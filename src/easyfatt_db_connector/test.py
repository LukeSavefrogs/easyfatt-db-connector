from pathlib import Path
import shutil

import sqlalchemy
import sqlalchemy_firebird

import urllib.parse


from easyfatt_db_connector.core.methods.sqlalchemy import EasyfattDB

database_path = Path("~/Documents/Danea Easyfatt/TestArchivio.eft").expanduser()


# Dynamic table
from easyfatt_db_connector.orm.dynamic import table_factory

# Static table
from easyfatt_db_connector.orm.static import TDocRighe

with EasyfattDB(database_path).connect() as conn:
    # Dynamic table
    TAnagrafica = table_factory("TAnagrafica", conn.engine)
    
    query = sqlalchemy.select(
        TAnagrafica.IDAnagr,
        TAnagrafica.CodAnagr,
        TAnagrafica.Nome,
        TAnagrafica.Indirizzo,
        TAnagrafica.Cap,
    )

    for row in conn.execute(query):
        print(row)

    # Static table
    query = TDocRighe.__table__.select()
    for row in conn.execute(query):
        print(row)