""" This package allows to interact with the Easyfatt database. """
from .core.connection import EasyfattFDB

# Import the XML parser
from .xml import read_xml