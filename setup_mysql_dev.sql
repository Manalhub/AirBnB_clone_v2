-- Create the hbnb_dev_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
