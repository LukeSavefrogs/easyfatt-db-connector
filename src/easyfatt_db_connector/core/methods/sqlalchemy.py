from __future__ import annotations
from contextlib import contextmanager
import time

from pathlib import Path
import shutil

from fdb.ibase import charset_map

import sqlalchemy
import sqlalchemy_firebird

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


    def create_engine(self, username=None, password=None, database_path: Path=None):
        connection_url = sqlalchemy.URL.create(
            drivername="firebird",
            username=self.db_username if username is None else username,
            database=str(self.archive_path.resolve() if database_path is None else database_path.resolve()),
            query={
                "fb_library_name": str(self.firebird_path / "fbembed.dll"),
                # "user": self.db_username if username is None else username
            }
        )
        return sqlalchemy.create_engine(connection_url, echo=False)
    
    @contextmanager
    def connect(self, engine: sqlalchemy.engine.base.Engine = None):
        """Connect to the database and return a connection object.

        Can be used as a context manager.

        Args:
            engine (sqlalchemy.engine.base.Engine, optional): The engine that will be used to connect to the database. Defaults to None.

        Yields:
            sqlalchemy.engine.base.Connection: The connection object.
        """
        temp_database = None

        if engine is None:
            temp_database = Path(f"{self.archive_path}.tmp~")
            shutil.copy(self.archive_path, temp_database)
    
            engine = self.create_engine(database_path=temp_database)

        try:
            with engine.connect() as connection:
                yield connection

            if temp_database is not None:
                engine.dispose()
            
        except sqlalchemy.exc.OperationalError as e:
            if "lock manager" in str(e):
                raise FirebirdClientError(
                    f"The database '{self.archive_path}' is locked. Close Easyfatt and try again."
                )
            else:
                raise
        finally:
            if temp_database is not None:
                try:
                    engine.dispose()
                except:
                    pass
                temp_database.unlink(missing_ok=True)



if __name__ == "__main__":
    database_path = Path("~/Documents/Danea Easyfatt/TestArchivio.eft").expanduser()

    db = EasyfattDB(database_path)
    print(f"- Is database locked? {db.is_locked()}")
