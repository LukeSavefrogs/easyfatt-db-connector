import sqlalchemy
import sqlalchemy_firebird

from sqlalchemy.orm.decl_api import DeclarativeMeta

__all__ = ["table_factory"]

Base = sqlalchemy.orm.declarative_base()

def table_factory(name: str, engine: sqlalchemy.Engine) -> DeclarativeMeta:
	""" Dynamically create a `DeclarativeMeta` class which instance can be used for SQL queries.
	
	This function can be useful in the following cases:
	- The static declaration is somehow broken for a specific table
	- A table is not present in the static declaration

	!!! Warning
		Always prefere static classes (`easyfatt_db_connector.orm.static`) instead of dynamically generated ones.
		This gives you intellisense over the table and allows for faster and easier development.

	Args:
		name (str): The name of the table
		engine (sqlalchemy.Engine): The engine object.

	Returns:
		sqlalchemy.orm.decl_api.DeclarativeMeta: The clas that will be used to perform queries on.
	
	!!! Example
		The following example shows how to execute queries on a hypotetical table `TTable` which 
		is not present among the static definitions:
		```
		TTable = table_factory("TTable", engine)
		with engine.connect() as conn:
			query = TTable.__table__.select()
			for row in conn.execute(query):
				print(row)
		```
	"""
	return type(name, (Base,),{
		"__table__": sqlalchemy.Table(name, Base.metadata, autoload_with=engine),
		"__tablename__": name
	})