-- creates the database hbtn_0d_usa and table states on my MySQL server.
   -- states description:
      -- id INT unique - auto generated, cannot be null, is a primary key
      -- name VARCHAR(256) - cannot be null
   -- If the table hbtn_0d_usa already exists, script shouldn't fail
   -- If the table states already exists, script shouldn't fail

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (`id` INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
       `name` VARCHAR(256));