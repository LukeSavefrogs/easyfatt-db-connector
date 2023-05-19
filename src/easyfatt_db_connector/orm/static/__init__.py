""" Static definitions for all the models.

All the models were generated using [sqlacodegen](https://github.com/agronholm/sqlacodegen).

To use a model `import` it and use it as follows:
```python
from easyfatt_db_connector.orm.static import TDocRighe

with engine.connect() as conn:
    query = TDocRighe.__table__.select()
    for row in conn.execute(query):
        print(row)
```
"""
from .models import *