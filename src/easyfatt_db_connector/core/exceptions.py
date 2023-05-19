""" Exceptions used throughout the project """


class EasyfattDBConnectorError(Exception):
    """A base class for exceptions coming from the `easyfatt-db-connector` project."""


class FirebirdClientError(EasyfattDBConnectorError):
    """An error concerning the Firebird client."""
