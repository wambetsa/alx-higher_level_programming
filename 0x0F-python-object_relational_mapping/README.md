# 0x0F. Python - Object-relational mapping
Using MySQL to create databases and Python to retrieve data from database

## Technologies and Skills Needed:
Which set of technologies are essential?
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
Why Python virtual environment/venv? Venv allows installation of specific dependencies for this python project. First, install venv. How? :
- $\textcolor{yellowgreen}{sudo\ apt-get\ install\ python3.8-venv}$
- $\textcolor{yellowgreen}{python3\ -m\ venv\ venv}$
- $\textcolor{yellowgreen}{source\ venv/bin/activate}$

## Install MySQLdb module version 2.0.x
For installing MySQLdb, we need to have MySQL installed: Where? On Linux or WSL. How? :
- $\textcolor{yellowgreen}{sudo\ apt-get\ install\ python3-dev}$
- $\textcolor{yellowgreen}{sudo\ apt-get\ install\ libmysqlclient-dev}$
- $\textcolor{yellowgreen}{sudo\ apt-get\ install\ zlib1g-dev}$
- $\textcolor{yellowgreen}{sudo\ pip3\ install\ mysqlclient}$
- $\textcolor{yellowgreen}{...}$
- $\textcolor{yellowgreen}{python3}$
- \>>> import MySQLdb
- \>>> MySQLdb.version_info 
- (2, 0, 3, 'final', 0)

## Install SQLAlchemy module version 1.4.x
How? :
- $\textcolor{yellowgreen}{sudo\ pip3\ install\ SQLAlchemy}$
- $\textcolor{yellowgreen}{...}$
- $\textcolor{yellowgreen}{python3}$
- \>>> import sqlalchemy
- \>>> sqlalchemy.__version__ 
- '1.4.22'

## Run SQL and Python Files
How do I run my MySQL scripts to create my database, create table, and insert data? :
- $\textcolor{yellowgreen}{cat\ mysqlfilename.sql\ |\ mysql\ -uroot\ -p}$

How do I run my python scripts to interact with database datasets?

If pyscript expect params such as username,  password, database name, run as follows:
- $\textcolor{yellowgreen}{./mypythonscript.py\ root\ root\ dbname}$

If pyscript doesn't expect any params, run py script as follows:
- $\textcolor{yellowgreen}{./mypythonscript.py}$

##### NB: It's important to note that constructing SQL queries by concatenating strings with user-provided input leaves your application vulnerable to SQL injection attacks. It's highly discouraged to construct queries this way. Instead, you should use parameterized queries or ORM libraries like SQLAlchemy to safely execute SQL queries with user input.

##### Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

#### FOR MORE INFO REFERENCE: 3-my_safe_filter_states.py vs 2-my_filter_states.py
### Author: Emmanuel Wambetsa Shitseswa
- dev wambetsa
