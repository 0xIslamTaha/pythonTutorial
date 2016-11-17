'''
- Refrance : https://pythonschool.net/databases/introduction-to-databases/
- A "database" is a organised body of related information that you can access in a clearly defined way.
- A "database management system" controls your access to the database and enables you to define, create and
maintain that database.

- We will use SQLite as it is provided as part of the standard Python library and provides us with all of the
 functionality that is necessary to teach databases at A-Level.
'''

import sqlite3
"Creating a new database in Python"
with sqlite3.connect('MyFirstDB.db') as db:
    pass

'''
The above statement will connect to the database with the provided name. If there is no file with the given name
 then it will create a new file with this name, otherwise it will open the existing file at this location.
'''
