# Datastore Boilerplate

## `datastore.py`

``` python
import sqlite3

class Datastore:
    
    def __init__(self, db_file_name: str):
        """
        Initate datastore object
        """
        
        self.connection = sqlite3.connect(db_file_name)
        self.cursor = self.connection.cursor()
        
        
    def __del__(self):
        """
        Writes data from cache to drive and then closes connection
        """
        self.connection.close()
```

## `test.py`

``` python
from datastore import Datastore

db = Datastore("netflix.db")
```

