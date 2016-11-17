'''
- A database is only useful when it has a clearly defined data model. This means that you have described how the data
 should be structured and added any constraints that are necessary. This structure is defined as an "entity-relationship
 model" and then implemented using the structured query language or SQL for short.

- In general you can think of an entity as an object or person in your system.
 Example : Products and Customers for a coffe shop

- Separate entities in the system may be related to one another. For example, a product may be purchased by customers
 we can represent this as an entity-relationship diagram. We call this the degree of the relationship.
 * Degree Type:
    one-to-one
    one-to-many
    many-to-one
    many-to-many

- A single entity will have various attributes to represent its characteristics.
Each attribute will have an attribute name (to describe the characteristic) and
an attribute type (what kind of data it is).

- We can describe product using an entity description
Example :
    Product(ProductID,Name,Price)
        ProductID : This provides us with an obvious unqiue identifier for each product, making it easy to locate product.
        NAme : Piece of data
        Price : Piece of data

- SQL can be separated into two parts:
    Data Definition Language (DDL)
        used to create the database structure
    Data Manipulation Language (DML)
        used to insert, delete, update, search and sort data in the database

- Create table statement
    To implement the product entity we must use the create table statement.
    Note: entity is used to refer to the abstract representation and table to refer to the actual implementation.
'''

import sqlite3

def create_table(db_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

if __name__ == '__main__':
    db_name = 'MyFirstDB.db'

    sql = '''CREATE TABLE Product
            (ProductID integer,
            Name text,
            Price real,
            PRIMARY KEY(ProductID))'''
    create_table(db_name, sql)
