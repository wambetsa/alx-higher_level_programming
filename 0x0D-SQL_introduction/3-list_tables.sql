-- a script that lists all tables in a database in my MYSQL Server
-- The database name is passed as an argument ofmysql command
USE `$$1`;
SHOW TABLES;
