# 0x0F. Python - Object-relational mapping
Using MySQL to create databases
Using Python to Select or retrieve data from database

## Technologies Needed:
- Python
- OOP
- SQL
- MySQL
- ORM
- SQLAlchemy

# Background Context
In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, we will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

# Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
- sudo apt-get install python3.8-venv
- python3 -m venv venv
- source venv/bin/activate

# Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04
- sudo apt-get install python3-dev
- sudo apt-get install libmysqlclient-dev
- sudo apt-get install zlib1g-dev
- sudo pip3 install mysqlclient
- ...
- python3
- \>>> import MySQLdb
- \>>> MySQLdb.version_info 
- (2, 0, 3, 'final', 0)

# Install SQLAlchemy module version 1.4.x
- sudo pip3 install SQLAlchemy
- ...
- python3
- \>>> import sqlalchemy
- \>>> sqlalchemy.__version__ 
- '1.4.22'

### Author: Emmanuel Wambetsa Shitseswa (dev wambetsa)