-- Filename: 1-create_database_if_missing.sql

-- Check if the database exists
SELECT COUNT(*) INTO @db_exists FROM information_schema.schemata WHERE schema_name = 'hbtn_0c_0';

-- If the database does not exist, create it
SET @create_query = IF(@db_exists = 0, 'CREATE DATABASE hbtn_0c_0;', '');

-- Execute the create query
PREPARE create_query FROM @create_query;
EXECUTE create_query;
DEALLOCATE PREPARE create_query;
