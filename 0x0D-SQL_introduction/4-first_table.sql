-- Filename: 4-first_table.sql

-- Check if the table exists
SELECT COUNT(*) INTO @table_exists FROM information_schema.tables WHERE table_schema = DATABASE() AND table_name = 'first_table';

-- If the table does not exist, create it
SET @create_query = IF(@table_exists = 0, 'CREATE TABLE first_table (id INT, name VARCHAR(256));', '');

-- Execute the create query
PREPARE create_query FROM @create_query;
EXECUTE create_query;
DEALLOCATE PREPARE create_query;
