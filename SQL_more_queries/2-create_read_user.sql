-- Create the database hbtn_0d_2 and user_0d_2 with specific privileges.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF NOT EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
