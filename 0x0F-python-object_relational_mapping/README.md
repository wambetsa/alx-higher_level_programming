# 0x0F. Python - Object-relational mapping
Using MySQL to create databases and Python to retrieve data from database

## Technologies and Skills Needed:
- Python
- OOP
- SQL
- MySQL
- ORM
- SQLAlchemy

## Background Context
In this project, we will link two amazing worlds: Databases and Python!

First, we will use the module MySQLdb to connect to a MySQL database and execute our SQL queries.

Second, we will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

Difference: no more SQL queries! Indeed, Why? Coz ORM abstracts data storage to the usage. With an ORM, our biggest concern will be “What can we do with our objects” and not “How this object is stored? where? when?”. We won’t write any SQL queries only Python code. Last thing, our code won’t be “storage type” dependent. We will be able to change our storage easily without re-writing our entire project.

## Install and activate venv
We will create a Python Virtual Environment, allowing us to install specific dependencies for this python project, we will install venv. How? :
- sudo apt-get install python3.8-venv
- python3 -m venv venv
- source venv/bin/activate

## Install MySQLdb module version 2.0.x
For installing MySQLdb, we need to have MySQL installed: How? :
- sudo apt-get install python3-dev
- sudo apt-get install libmysqlclient-dev
- sudo apt-get install zlib1g-dev
- sudo pip3 install mysqlclient
- ...
- python3
- \>>> import MySQLdb
- \>>> MySQLdb.version_info 
- (2, 0, 3, 'final', 0)

## Install SQLAlchemy module version 1.4.x
- sudo pip3 install SQLAlchemy
- ...
- python3
- \>>> import sqlalchemy
- \>>> sqlalchemy.__version__ 
- '1.4.22'

## Run SQL and Python Files
How do I run my MySQL scripts to create my database, create table, and insert data? :
- cat my_sql_filename.sql | mysql -uroot -p
How do I run my python scripts to interact with database datasets?

If our pyscript expect params such as username,  password, database name, run as follows:
- ./my_python_script.py root root database_name

If our pyscript doesn't expect any params, run py script as follows:
- ./my_python_script.py

### Author: Emmanuel Wambetsa Shitseswa (dev wambetsa)