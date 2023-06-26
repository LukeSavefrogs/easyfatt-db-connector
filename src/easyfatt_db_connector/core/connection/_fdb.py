from contextlib import contextmanager
import shutil
from typing import Any, Generator, Literal, Optional
from pathlib import Path

import fdb

from easyfatt_db_connector.core.exceptions import FirebirdClientError
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
        if self.is_locked():
            raise FirebirdClientError(
                f"The database '{self.archive_path}' is locked. Close Easyfatt and try again."
            )
        
        temp_database = Path(f"{self.archive_path}.tmp~")
        shutil.copy(self.archive_path, temp_database)

        connection = None
        try:
            connection: TypedFDBConnection = fdb.connect(
                database=str(self.archive_path),
                user=self.db_username,
                password=self.db_password if self.db_password else None,
                charset=self.db_charset,
                fb_library_name=str(self.firebird_path / "fbembed.dll"),
            )
            yield connection
        
        except Exception:
            raise

        finally:
            if connection is not None:
                connection.close()

            if temp_database is not None:
                temp_database.unlink(missing_ok=True)



if __name__ == "__main__":
    database_path = Path("~/Documents/Danea Easyfatt/TestArchivio.eft").expanduser()

    db = EasyfattFDB(database_path)
    print(f"- Is database locked: {db.is_locked()}")
    print(f"- Connection string : '{db.get_connection_string()}'")

    with db.connect() as connection:
        # Informazioni generali sul DB
        print(f"Version    : {connection.version}")
        print(f"Created on : {connection.creation_date}")
        print(f"DB Name    : {connection.database_name}")
        print(f"ReadOnly   : {connection.isreadonly()}")

        cur = connection.cursor()
        print(cur.execute("select * from RDB$ROLES").fetchall())