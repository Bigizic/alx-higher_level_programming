-- a script that creates the MySQL server user user_0d_1 and sets a pswd
-- Also grant all privilage to the user on all databases and tables
-- Databases and tables is represented by *.*

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
