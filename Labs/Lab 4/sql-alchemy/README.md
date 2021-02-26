#### Lab 4 Sql Alchemy Postgres:

1. Google Docs Link : https://docs.google.com/document/d/1jVJlhQrkNxxw7-VSGBtybRtXe4ZYS6UMn56IS1vhCW8/edit?usp=sharing

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1jVJlhQrkNxxw7-VSGBtybRtXe4ZYS6UMn56IS1vhCW8#0

## SQL Alchemy

SQLAlchemy is a library that facilitates the communication between Python programs and databases. 
This library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements. 

#### ORM?

Object Relational Mapper, also known as ORM, is a technique used to write database queries using the object-oriented paradigm of your preferred language (in this case, Python)

Think of ORM as a translator that converts code from one set of abstractions to another - Python to SQL in this case.

#### How can SQLAlchemy help?

SQLAlchemy provides:
- A standard interface that allows developers to create database-agnostic code to communicate with a wide variety of database engines
- Enables Python developers to create applications that communicate to different database engines through the same API


Most of the popular relational databases available out there adhere to the SQL standard, but they also introduce proprietary variations. These variations are the solely responsible for the existence of dialects.

Getting first 10 records on SQL Server
```
SELECT TOP 10 * FROM table;
```
vs. getting first 10 rows on MySQL
```
SELECT * FROM table LIMIT 10;
```
For SQLAlchemy to know precisely what query to issue, it needs to be aware of the type of the database that it is dealing with. This is exactly what Dialects do.

#### How can SQLAlchemy help?

- Speeding up web development since we don’t have to switch back and forth between writing Python and SQL
- Eliminating repetitive code
- Streamlining the workflow and queries the data more efficiently
- Abstracting away the database system so switching between different databases becomes smooth
- Generating boilerplate code for the basic CRUD operations

References: <br>
(1) [auth0 blog](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/?utm_source=medium&utm_medium=sc&utm_campaign=sqlalchemy_python)


### Requirements 

```
pip install sqlalchemy
pip install psycopg2-binary
```

### Getting Started

Enter your connection details to the PostgreSQL server in `base.py` - in my case it is 
```
postgresql://localhost:5432/postgres
```
since I have no username and password to my database. Creating an engine does not connect to the database instantly. This process is postponed to when it's needed (like when we submit a query, or when create/update a row in a table).

- `base.py` contains the connection params to connect to the instance
- `customer.py` - A sample Python classes containing 5 attributes that we'd like to be converted to a table
- `main.py` - Insert data using the newly created class
- `queries.py` - Querying the table

### Additional Resources

- https://www.sqlalchemy.org/
- https://docs.sqlalchemy.org/en/13/orm/tutorial.html
