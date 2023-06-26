from pathlib import Path


DEFAULT_FIREBIRD_LOCATION = Path("~/.cache/firebird-embedded/").expanduser()

DEFAULT_DATABASE_USERNAME = "SYSDBA"
DEFAULT_DATABASE_PASSWORD = "masterkey"
DEFAULT_DATABASE_CHARSET = "WIN1252"
