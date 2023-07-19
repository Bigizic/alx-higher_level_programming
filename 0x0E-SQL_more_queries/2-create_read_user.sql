-- a script that creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 only have SELECT PRIVILAGE in the database created
-- user_0d_2 has a password

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON *hbtn_0d_2.table* TO 'user_0d_2'@'localhost';
