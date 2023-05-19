from __future__ import annotations
from typing import Any, Literal, Optional

from pathlib import Path
import shutil

import fdb
from fdb.fbcore import _RowMapping
from fdb.ibase import charset_map

from easyfatt_db_connector.core.exceptions import FirebirdClientError
from easyfatt_db_connector.constants import (
    DEFAULT_DATABASE_CHARSET,
    DEFAULT_DATABASE_PASSWORD,
    DEFAULT_DATABASE_USERNAME,
    DEFAULT_FIREBIRD_LOCATION,
)


class EasyfattDB(object):
    archive_path: Path
    firebird_path: Path

    db_username: str
    db_password: str
    db_charset: str | None

    def __init__(
        self,
        archive_path: str | Path,
        firebird_path: Path = DEFAULT_FIREBIRD_LOCATION,
        db_user=DEFAULT_DATABASE_USERNAME,
        db_password=DEFAULT_DATABASE_PASSWORD,
        db_charset: str | None = DEFAULT_DATABASE_CHARSET,
    ):
        """Initialize a new EasyfattDB object and connect to the DB.

        Args:
            archive_path (str | Path): The path to the database
            firebird_path (Path, optional): The Firebird Embedded installation path
            db_user (str, optional): The user that will be used to connect to the database.
            db_password (str, optional): The password that will be used to connect to the database.
            db_charset (str | None, optional): The character set that will be used to interpret data.
        """
        self.archive_path = Path(archive_path).expanduser().resolve()
        self.firebird_path = Path(firebird_path).expanduser().resolve()

        if db_charset not in charset_map.keys():
            supported_charsets = ", ".join([str(charset) for charset in charset_map.keys()])

            raise FirebirdClientError(
                f"Character set '{db_charset}' not valid. Use one of '{supported_charsets}'"
            )

        self.db_username = db_user
        self.db_password = db_password
        self.db_charset = db_charset

        # Check if Firebase Embedded is installed
        if not self.firebird_path.exists():
            raise FirebirdClientError(f"The path '{self.firebird_path}' does not exist.")

        if not (self.firebird_path / "fbembed.dll").exists():
            raise FirebirdClientError(
                f"The path '{self.firebird_path}' MUST contain the file 'fbembed.dll'."
            )

        # Questa riga è fondamentale!
        # Stiamo dicendo a fdb dove si trovano i binari di Firebird Embedded (vedi https://stackoverflow.com/a/62245011/8965861)!
        fdb.load_api(str(self.firebird_path / "fbembed.dll"))

    def _connect(self):
        try:
            # Use `WIN1252` instead of `UTF8` to fix error "SQLCODE: -204 block size exceeds implementation restriction"
            # See https://stackoverflow.com/q/40170882/8965861
            print(f"Connecting to database '{self.archive_path}'")
            fdb.connect(
                database=str(self.archive_path),
                user=self.db_username,
                # password=self.db_password,
                charset=self.db_charset,
            )
        except (fdb.DatabaseError, UnicodeDecodeError) as e:
            if "codec can't decode byte" in str(e) or "lock manager" in str(e):
                return True
            else:
                raise
        else:
            return False

    def is_locked(self):
        try:
            # Use `WIN1252` instead of `UTF8` to fix error "SQLCODE: -204 block size exceeds implementation restriction"
            # See https://stackoverflow.com/q/40170882/8965861
            print(f"Connecting to database '{self.archive_path}'")
            fdb.connect(
                database=str(self.archive_path),
                user=self.db_username,
                # password=self.db_password,
                charset=self.db_charset,
            )
        except (fdb.DatabaseError, UnicodeDecodeError) as e:
            if "codec can't decode byte" in str(e) or "lock manager" in str(e):
                return True
            else:
                raise
        else:
            return False


if __name__ == "__main__":
    database_path = Path("~/Documents/Danea Easyfatt/TestArchivio.eft").expanduser()

    db = EasyfattDB(database_path)
    print(f"- Is database locked? {db.is_locked()}")
