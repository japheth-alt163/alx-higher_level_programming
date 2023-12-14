-- Save the script in a file, e.g., 2-create_read_user.sql

-- Content of 2-create_read_user.sql
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
