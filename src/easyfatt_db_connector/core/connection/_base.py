""" Generic class for EasyfattDB. """
from pathlib import Path
from typing import Optional, Union
import urllib.parse

import fdb

import easyfatt_db_connector.utils.downloader as firebird_downloader
from easyfatt_db_connector.constants import (
    DEFAULT_DATABASE_CHARSET,
    DEFAULT_DATABASE_PASSWORD,
    DEFAULT_DATABASE_USERNAME,
    DEFAULT_FIREBIRD_LOCATION,
)
from easyfatt_db_connector.core.exceptions import FirebirdClientError


class EasyfattDBGeneric(object):
    """ Generic class for EasyfattDB. """
    archive_path: Path
    firebird_path: Path

    db_username: str
    db_password: str
    db_charset: Optional[str]

    def __init__(
        self,
        archive_path: Union[str, Path],
        firebird_path: Path = DEFAULT_FIREBIRD_LOCATION,
        download_firebird: bool = False,
        username: str = DEFAULT_DATABASE_USERNAME,
        password: str = DEFAULT_DATABASE_PASSWORD,
        charset: Optional[str] = DEFAULT_DATABASE_CHARSET,
    ) -> None:
        """Initialize a new EasyfattDB object and connect to the DB.

        Args:
            archive_path (str | Path): The path to the database file (with `.eft` extension).
            firebird_path (Path, optional): Path to the `fbembed.dll` parent folder. Defaults to DEFAULT_FIREBIRD_LOCATION.
            download_firebird (bool, optional): Whether the Firebird embedded driver should be automatically downloaded if not found. DO NOT USE IN PRODUCTION. Defaults to False.
            username (str, optional): Username used to connect to the database. Defaults to DEFAULT_DATABASE_USERNAME.
            password (str, optional): Password used to connect to the database. Defaults to DEFAULT_DATABASE_PASSWORD.
            charset (str | None, optional): Charset to use with the connection. Defaults to DEFAULT_DATABASE_CHARSET.
        """
        self.archive_path = Path(archive_path).expanduser().resolve()
        self.firebird_path = Path(firebird_path).expanduser().resolve()
        
        if not self.archive_path.exists():
            raise FirebirdClientError(f"The path '{self.archive_path}' does not exist.")
        
        # Check if the charset is supported
        if charset is None:
            self.db_charset = None
        elif charset.upper() in fdb.charset_map.keys():
            self.db_charset = charset
        elif charset in fdb.charset_map.values():
            inverted_map = {v: k for k, v in fdb.charset_map.items()}
            self.db_charset = inverted_map[charset]
        else:
            supported_charsets = ", ".join([str(charset) for charset in fdb.charset_map.keys()])
            raise FirebirdClientError(
                f"Character set '{charset}' not valid. Use one of '{supported_charsets}'"
            )

        self.db_username = username
        self.db_password = password
        self.db_charset = charset

        # Check if Firebase Embedded is installed
        try:
            if not self.firebird_path.exists():
                raise FirebirdClientError(f"The path '{self.firebird_path}' does not exist.")

            elif not (self.firebird_path / "fbembed.dll").exists():
                raise FirebirdClientError(
                    f"The path '{self.firebird_path}' MUST contain the file 'fbembed.dll'."
                )
        except FirebirdClientError:
            if download_firebird:
                print("Downloading Firebird Embedded...")
                firebird_downloader.download("R2_5_9", firebird_path=self.firebird_path)
            else:
                raise

    def __repr__(self) -> str:
        return f"<EasyfattDBGeneric: {self.archive_path}>"
    
    def get_connection_string(self, username=None, charset=None, protocol="firebird") -> str:
        """Returns the URI to connect to the database.
        
        Args:
            username (str, optional): Username used to connect to the database. Defaults to None.
            charset (str, optional): Charset to use with the connection. Defaults to None.
            protocol (str, optional): Protocol to use. Defaults to "firebird".
        """
        parameters = urllib.parse.urlencode({
            "charset": self.db_charset if charset is None else charset,
            "fb_library_name": str(self.firebird_path / "fbembed.dll"),
            "user": self.db_username if username is None else username
        }, quote_via=urllib.parse.quote)
        
        # 'localhost' MUST NOT be used, otherwise the connection will fail with error:
        #
        #       sqlalchemy.exc.DatabaseError: (fdb.fbcore.DatabaseError) ('Error while connecting to database:\n- SQLCODE: -902\n- Your 
        #       user name and password are not defined. Ask your database administrator to set up a Firebird login.', -902, 335544472)  
        return f"{protocol}://{self.db_username}:{self.db_password}@/{self.archive_path}?{parameters}"
    

    def is_locked(self):
        """ Check if the database is locked.
        
        TODO: Decide wether to make this method static or move it to the global scope and then reference it.
        This way could be parametrized to accept a path.

        FIXME: this method may cause your program to hang briefly (few seconds) when exiting.
        This behaviour could be caused by a global object that gets instantiated by the 
        `fdb.connect` call and it takes some time to be destroyed by the GC at the end.

        Returns:
            bool: Whether the database is locked or not.
        """
        try:
            # Use `WIN1252` instead of `UTF8` to fix error "SQLCODE: -204 block size exceeds implementation restriction"
            # See https://stackoverflow.com/q/40170882/8965861
            fdb.connect(
                database=str(self.archive_path),
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
            
            print(f"SQLCODE: {sqlcode} (error: {error_message})")
            
            if "codec can't decode byte" in error_message or "lock manager" in error_message:
                return True
            elif sqlcode == -902: # File used by another process (Error while connecting to database:\n- SQLCODE: -902\n- I/O error during "CreateFile (open)" operation for file "C:\\USERS\\{...}.EFT"\n- Error while trying to open file)
                return True
            else:
                raise
        else:
            return False