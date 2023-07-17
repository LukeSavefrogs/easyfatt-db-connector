from dataclasses import dataclass


@dataclass
class BaseField(object):
    """ Basic implementation of an XML field.

    Allows to define relationships between XML elements and Python classes.
    """

    target: type = None
    """ Class to map the XML element to. """


@dataclass
class Field(BaseField):
    """ Represents an XML field.

    Allows to define relationships between XML elements and Python classes.
    """

    tag: str = None
    """ Override XML tag name. """

    is_parent: bool = False
    """ Whether the XML element is a list of elements. """

    child: "Field" = None
    """ Children XML elements. """


@dataclass
class FieldGroup(BaseField):
    """ This special field allows to group multiple XML fields together under the same dataclass.

    This is useful when many XML fields are related to each other and it is more convenient to
    assign them to the attributes of a single dataclass.
    """
    ...
