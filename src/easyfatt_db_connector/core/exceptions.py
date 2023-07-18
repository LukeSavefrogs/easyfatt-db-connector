""" Exceptions used throughout the project """


class EasyfattDBConnectorError(Exception):
    """A base class for exceptions coming from the `easyfatt-db-connector` project."""


class EasyfattXMLError(Exception):
    """A base class for exceptions coming from the `easyfatt-db-connector.xml` project."""


class FirebirdClientError(EasyfattDBConnectorError):
    """An error concerning the Firebird client."""

class DatabaseLockedError(EasyfattDBConnectorError):
    """ Error raised when the Firebird database is locked. """

class TypeConversionError(EasyfattXMLError):
    """ Error raised when a type conversion of an XML field is not possible. """