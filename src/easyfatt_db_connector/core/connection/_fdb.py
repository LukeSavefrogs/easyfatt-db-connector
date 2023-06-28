from contextlib import contextmanager
import os
import shutil
import tempfile
from typing import Any, Generator, Literal, Optional
from pathlib import Path

import fdb

from easyfatt_db_connector.core.exceptions import DatabaseLockedError
from easyfatt_db_connector.core.connection._base import EasyfattDBGeneric

class TypedFDBConnection(fdb.Connection):
    """ Stub class used only to provide correct type hjinting to child classes,
    since the `fdb.Connection` class does not provide any type hinting for some return values.
    
    DO NOT USE THIS CLASS DIRECTLY: The methods are not implemented and will raise a NotImplementedError.
    """
    def execute_immediate(self) -> None:
        raise NotImplementedError

    def cursor(self) -> fdb.Cursor:
        raise NotImplementedError


class EasyfattFDB(EasyfattDBGeneric):
    def _connect(self, database_path: Path) -> TypedFDBConnection:
        """ Wrapper around `fdb.connect` which handles some edge cases.

        Args:
            database_path (Path): The path to the database file.

        Raises:
            FirebirdClientError: If the database is locked.
        """
        try:
            # Use `WIN1252` instead of `UTF8` to fix error "SQLCODE: -204 block size exceeds implementation restriction"
            # See https://stackoverflow.com/q/40170882/8965861
            return fdb.connect(
                database=str(database_path),
                user=self.db_username,
                password=self.db_password if self.db_password else None,
                charset=self.db_charset,
                fb_library_name=str(self.firebird_path / "fbembed.dll"),
            )
        except (fdb.DatabaseError, UnicodeDecodeError) as e:
            error_message = str(e)

            try:
                sqlcode = e.args[1]
            except:
                sqlcode = None
            
            if (
                ("codec can't decode byte" in error_message) or   # Not sure why, but sometimes this error pops up when the database is locked
                ("lock manager error" in error_message) or        # Database locked
                (sqlcode == -902)                                 # Database file used by another process
            ):
                raise DatabaseLockedError(
                    f"The database '{self.archive_path}' is locked. Close Easyfatt and try again."
                )
            
            # Error is not handled, propagate it to the caller
            raise
        
    """ Implementation of the `EasyfattDBGeneric` class using the `fdb` library. """
    @contextmanager
    def connect(self) -> Generator[TypedFDBConnection, None, None]:
        """Connect to the database and return a connection object.

        Can be used as a context manager.

        Yields:
            TypedFDBConnection: The connection object.
        
        Raises:
            FirebirdClientError: If the database is locked.
        """     
        handle, path = tempfile.mkstemp(prefix=f"{self.archive_path.stem}-", suffix=".eft.tmp~")
        os.close(handle)

        temp_database = Path(path)
        shutil.copy(self.archive_path, temp_database)

        connection = None
        try:
            connection: TypedFDBConnection = self._connect(temp_database)
            yield connection

        except Exception:
            raise

        finally:
            if connection is not None:
                connection.close()

            temp_database.unlink(missing_ok=True)



if __name__ == "__main__":
    database_path = Path("~/Documents/Danea Easyfatt/TestArchivio.eft").expanduser()

    db = EasyfattFDB(database_path)
    # print(f"- Is database locked: {db.is_locked()}")
    print(f"- Connection string : '{db.get_connection_string()}'")

    with db.connect() as connection:
        # Informazioni generali sul DB
        print(f"Version    : {connection.version}")
        print(f"Created on : {connection.creation_date}")
        print(f"DB Name    : {connection.database_name}")
        print(f"ReadOnly   : {connection.isreadonly()}")

        cur = connection.cursor()
        print(cur.execute("select * from RDB$ROLES").fetchall())
    
    print(f"The end.")