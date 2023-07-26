# import os as _os
# import xml.dom.minidom as minidom
from typing import get_type_hints

import lxml.etree as ET

from easyfatt_db_connector.core.exceptions import TypeConversionError

from .fields import BaseField, Field, FieldGroup


class XMLMapper(object):
    """Base class for XML mappers.

    - Use the `__xml_mapping__` class attribute to map XML elements to class attributes.
    - Use the `__xml_name__` class attribute to override the name of the XML element the class refers to.
    """

    __xml_name__: str = ""
    """ Customize the name of the XML tag. 
    
    If not specified, it will be the set to the name of the class.
    """

    __xml_mapping__: dict[str, str] = None

    def __str__(self) -> str:
        attributes = [
            (f"{attr}='{value}'" if type(value) == str else f"{attr}={value}")
            for attr, value in self.__dict__.items()
        ]
        return f"{self.__class__.__name__}({', '.join(attributes)})"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __hash__(self) -> int:
        """ Returns a hash of the object. """
        return hash((type(self),) + tuple(
            [tuple(value) if type(value) == list else value for value in self.__dict__.values()]
        ))

    @classmethod
    def _get_xml_tag(cls) -> str:
        return cls.__xml_name__ if getattr(cls, "__xml_name__", None) else cls.__name__

    @classmethod
    def from_xml_string(cls, string: str, convert_types=True, *, _warn_untracked=True):
        """ Creates an instance of the class from an XML text.

        Args:
            string (str): The XML text to parse.
            convert_types (bool, optional): Whether to convert the types of the fields. Defaults to True.
            _warn_untracked (bool, optional): Whether to warn if there are untracked children (for internal use only). Defaults to True.
        
        Raises:
            NotImplementedError: If the class does not have an `__xml_mapping__` attribute or if is not a dictionary.
            TypeError: If the value of the `__xml_mapping__` attribute is not valid.
            TypeConversionError: If the type of the field is not supported.
            
        Returns:
            XMLMapper: An instance of the class.
        """
        return cls.from_xml(
            ET.fromstring(string),
            convert_types=convert_types,
            _warn_untracked=_warn_untracked,
        )

    @classmethod
    def from_xml(cls, element: ET._Element, convert_types=True, *, _warn_untracked=True):
        """ Creates an instance of the class from an XML text.
        
        Args:
            element (ET._Element): The XML element to parse.
            convert_types (bool, optional): Whether to convert the types of the fields. Defaults to True.
            _warn_untracked (bool, optional): Whether to warn if there are untracked children (for internal use only). Defaults to True.
            
        Raises:
            NotImplementedError: If the class does not have an `__xml_mapping__` attribute or if is not a dictionary.
            TypeError: If the value of the `__xml_mapping__` attribute is not valid.
            TypeConversionError: If the type of the field is not supported.
            
        Returns:
            XMLMapper: An instance of the class.
        """
        if getattr(cls, "__xml_mapping__", None) is None and type(cls.__xml_mapping__) != dict:
            raise NotImplementedError(
                "This class does not have an __xml_mapping__ attribute defined."
            )
        
        # Check if there are tags that are not tracked in the `__xml_mapping__` attribute
        # I did not use a list comprehension since it would have been too long and unreadable
        child_tags = []
        for child in cls.__xml_mapping__.values():
            if type(child) == str:
                child_tags.append(child)
            elif isinstance(child, FieldGroup):
                child_tags.extend(list(child.target.__xml_mapping__.values()))
            elif isinstance(child, Field):
                if getattr(child, "is_parent"):
                    child_tags.append(child.tag)
                elif getattr(child, "tag", None):
                    child_tags.append(child.tag)
                else:
                    child_tags.append(child.target._get_xml_tag())

        untracked_children = [
            child.tag for child in element.iterchildren() if child.tag not in child_tags
        ]

        if untracked_children and _warn_untracked:
            print(
                f"\nWARNING: A total of {len(untracked_children)} children are not tracked ({', '.join(untracked_children)}) in the `{cls.__name__}.__xml_mapping__` class attribute.\n"
            )

        xml_object = cls()
        for attr, target in cls.__xml_mapping__.items():
            # Fail if the attribute is of the wrong type
            if type(target) != str and not isinstance(target, BaseField):
                raise TypeError(f"target must be a string or Field, not {type(target)}")

            if isinstance(target, FieldGroup):
                setattr(
                    xml_object,
                    attr,
                    target.target.from_xml(element, convert_types=convert_types, _warn_untracked=False),
                )

            elif isinstance(target, Field):
                child_class_name = ""
                if getattr(target, "tag", None):
                    child_class_name = target.tag
                elif getattr(target, "target", None):
                    child_class_name = target.target._get_xml_tag()

                if getattr(target, "is_parent"):
                    children = element.xpath(
                        f"{child_class_name}/{target.child.target._get_xml_tag()}"
                    )

                    children_obj = [
                        target.child.target.from_xml(child_xml, convert_types=convert_types, _warn_untracked=_warn_untracked)
                        for child_xml in children
                    ]

                    setattr(xml_object, attr, children_obj)
                else:
                    child_element = element.find(child_class_name)

                    if child_element is not None:
                        setattr(
                            xml_object,
                            attr,
                            target.target.from_xml(child_element, convert_types=convert_types, _warn_untracked=_warn_untracked),
                        )
            else:
                element_text = ""

                # ---> XML Attribute
                if target.strip().startswith("@"):
                    element_text = element.get(target[1:])

                elif target.strip().upper() == "#TEXT":
                    element_text = element.text

                # ---> XML Child Element
                else:
                    child_element = element.find(target)

                    if child_element is None:
                        continue

                    element_text = child_element.text

                if not convert_types:
                    setattr(xml_object, attr, element_text)
                    continue

                # =======> Type conversion <=======
                expected_type = get_type_hints(cls)[attr]

                try:
                    converted_value = None
                    if expected_type == bool or "[bool]" in str(expected_type):
                        if element_text is None:
                            element_text = ""
                        converted_value = element_text.lower() == "true"

                    elif expected_type == int or "[int]" in str(expected_type):
                        if element_text is None:
                            element_text = 0
                        converted_value = int(element_text)

                    elif expected_type == float or "[float]" in str(expected_type):
                        if element_text is None:
                            element_text = 0
                        converted_value = float(element_text)

                    elif expected_type == str or "[str]" in str(expected_type):
                        if element_text is None:
                            element_text = ""
                        converted_value = str(element_text)

                    else:
                        converted_value = element_text

                except ValueError:
                    raise TypeConversionError(
                        f"Error while converting `{cls.__name__}.{attr}`: `{element_text}` cannot be converted to `{expected_type.__name__}`."
                    )
                else:
                    setattr(xml_object, attr, converted_value)

        return xml_object

    # def to_xml(self) -> ET.Element:
    #     if getattr(self, "__xml_mapping__", None) is None or self.__xml_mapping__ == {}:
    #         raise NotImplementedError(
    #             "This class does not have an __xml_mapping__ attribute defined."
    #         )

    #     custom_element_name = getattr(self, "__xml_name__", "")
    #     root = ET.Element(
    #         custom_element_name if custom_element_name else self.__class__.__name__
    #     )

    #     for attr, xml_tag in self.__xml_mapping__.items():
    #         if isinstance(xml_tag, Field):
    #             tag_name = ""
    #             if getattr(xml_tag, "tag", None):
    #                 tag_name = xml_tag.tag
    #             elif getattr(xml_tag, "target", None):
    #                 if getattr(xml_tag.target, "__xml_name__", None):
    #                     tag_name = xml_tag.target.__xml_name__
    #                 else:
    #                     tag_name = xml_tag.target.__name__
    #             print(tag_name)

    #         if not hasattr(self, attr):
    #             raise AttributeError(
    #                 f"Attribute {attr} not found in class {self.__class__.__name__}"
    #             )

    #         attribute_value = getattr(self, attr)

    #         if attribute_value is None:
    #             continue

    #         # ---> XML Attribute
    #         if xml_tag.startswith("@"):
    #             root.set(xml_tag[1:], python2xml(attribute_value))

    #         # ---> XML Child Element
    #         else:
    #             child_element = ET.Element(xml_tag)
    #             if isinstance(attribute_value, list):
    #                 for item in attribute_value:
    #                     if isinstance(item, XMLMapper):
    #                         child_element.append(item.to_xml())
    #                     else:
    #                         raise TypeError(
    #                             f"Item {item} is not an instance of XMLConverter"
    #                         )

    #                 child_element[:] = sorted(
    #                     child_element, key=lambda child: child.tag
    #                 )
    #             else:
    #                 child_element.text = python2xml(attribute_value)

    #             root.append(child_element)

    #     root[:] = sorted(root, key=lambda child: child.tag)

    #     return root

    # def to_xml_string(
    #     self, short_empty_elements=False, prettify=False, indent="    "
    # ) -> str:
    #     """Converts the object to an XML string.

    #     Args:
    #         short_empty_elements (bool, optional): Shorten empty elements. Defaults to False.
    #         prettify (bool, optional): Pretty print the XML. Defaults to False.
    #         indent (str, optional): Character used while pretty printing the XML. Defaults to "    ".

    #     Returns:
    #         str: string representation of the XML object.
    #     """
    #     xml_string = ET.tostring(
    #         self.to_xml(),
    #         method="xml",
    #         encoding="UTF-8",
    #         short_empty_elements=short_empty_elements,
    #         xml_declaration=True,
    #     ).decode("utf-8")

    #     if not prettify:
    #         return xml_string

    #     pretty_xml = minidom.parseString(xml_string).toprettyxml(indent=indent)
    #     pretty_xml = _os.linesep.join([s for s in pretty_xml.splitlines() if s.strip()])

    #     return pretty_xml
