-- Change collation in the hbtn_0c_0 database to utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Switch to the hbtn_0c_0 database
USE hbtn_0c_0;

-- Change collation for all tables in the database to utf8mb4_unicode_ci
-- This is an example; replace 'first_table' with the actual table names
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
