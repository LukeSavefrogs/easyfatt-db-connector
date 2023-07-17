from dataclasses import dataclass
import os as _os

import lxml.etree as ET
import xml.dom.minidom as minidom

from typing import get_type_hints


def python2xml(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return ""
    else:
        return str(value)


@dataclass
class Field(object):
    """Represents an XML field.

    Allows to define relationships between XML elements and Python classes.
    """

    target: type = None
    """ Class to map the XML element to. """

    tag: str = None
    """ Override XML tag name. """

    child: "Field" = None
    """ Children XML elements. """
    
    is_parent: bool = False
    """ Whether the XML element is a list of elements. """


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

    @classmethod
    def _get_xml_tag(cls) -> str:
        return cls.__xml_name__ if getattr(cls, "__xml_name__", None) else cls.__name__

    @classmethod
    def from_xml_string(cls, string: str):
        """Creates an instance of the class from an XML text."""
        return cls.from_xml(ET.fromstring(string))

    @classmethod
    def from_xml(cls, element: ET._Element):
        """Creates an instance of the class from an XML text."""
        if getattr(cls, "__xml_mapping__", None) is None:
            raise NotImplementedError(
                "This class does not have an __xml_mapping__ attribute defined."
            )

        # Check if there are tags that are not tracked in the `__xml_mapping__` attribute
        child_tags = [
            (
                child
                if type(child) == str
                else (child.tag if child.is_parent else child.target._get_xml_tag())
            )
            for child in cls.__xml_mapping__.values()
        ]
        untracked_children = [
            child.tag for child in element.iterchildren() if child.tag not in child_tags
        ]
        if untracked_children:
            print(f"\nWARNING: A total of {len(untracked_children)} children are not tracked ({', '.join(untracked_children)}) in the `{cls.__name__}.__xml_mapping__` class attribute.\n")

        xml_object = cls()
        for attr, target in cls.__xml_mapping__.items():
            # Fail if the attribute is of the wrong type
            if type(target) not in [str, Field]:
                raise TypeError(f"target must be a string or Field, not {type(target)}")

            if isinstance(target, Field):
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
                        target.child.target.from_xml(child_xml)
                        for child_xml in children
                    ]

                    setattr(xml_object, attr, children_obj)
                else:
                    setattr(
                        xml_object,
                        attr,
                        target.target.from_xml(element.find(child_class_name)),
                    )
            else:
                # ---> XML Attribute
                if target.startswith("@"):
                    setattr(xml_object, attr, element.get(target[1:]))

                # ---> XML Child Element
                else:
                    child_element = element.find(target)

                    if child_element is None:
                        continue

                    # =======> Type conversion <=======
                    expected_type = get_type_hints(cls)[attr]

                    element_text = child_element.text
                    if expected_type == bool or "[bool]" in str(expected_type):
                        if element_text is None:
                            element_text = ""
                        setattr(xml_object, attr, element_text.lower() == "true")
                    elif expected_type == int or "[int]" in str(expected_type):
                        if element_text is None:
                            element_text = 0
                        setattr(xml_object, attr, int(element_text))
                    elif expected_type == float or "[float]" in str(expected_type):
                        if element_text is None:
                            element_text = 0
                        setattr(xml_object, attr, float(element_text))
                    elif expected_type == str or "[str]" in str(expected_type):
                        if element_text is None:
                            element_text = ""
                        setattr(xml_object, attr, element_text)
                    else:
                        setattr(xml_object, attr, element_text)

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