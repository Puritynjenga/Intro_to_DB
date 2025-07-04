-- This script shows the full description of the 'books' table 
-- from the 'alx_book_store' database without using DESCRIBE or EXPLAIN.
-- The database name will be passed as an argument to the mysql command.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';