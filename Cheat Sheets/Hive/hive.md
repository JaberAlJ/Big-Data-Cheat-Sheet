# Hive Commands Cheat Sheet ✨ (Common Commands)

This section provides a quick reference for common ```hiveql and command-line interface (CLI) commands that are frequently used across various Hive table types and partitioning strategies. For more specific details on Internal, External, Static, or Dynamic Partitioned tables, please refer to their dedicated cheat sheets.

---

## I. Hive Shell Basics & Database Management 🚀

-   **Launch Hive CLI:**
```bash
hive
```
-   **Clear Hive Shell Screen:**
```hiveql
!clear;
```
-   **Exit Hive Shell:**
```hiveql
quit;
```

### Database Operations 🗄️

-   **Create a Database:**
```hiveql
CREATE DATABASE db_name;
```
-   **Show All Databases:**
```hiveql
SHOW DATABASES;
```
-   **Switch to a Database:**
```hiveql
USE db_name;
```
-   **Show Tables in Current Database:**
```hiveql
SHOW TABLES;
```

---

## II. Table Management & Schema Changes 🛠️

-   **Describe Table Schema (Basic):**
```hiveql
DESCRIBE table_name;
```
-   **Describe Table Schema (Formatted Details):**
*Found specifically in external table docs, but generally useful.*
```hiveql
DESCRIBE FORMATTED table_name;
```
-   **Add a New Column to a Table:**
```hiveql
ALTER TABLE table_name ADD COLUMNS (new_col_name datatype);
```
-   **Drop a Table:** 🗑️
```hiveql
DROP TABLE table_name;
```
> [!IMPORTANT]
> *The behavior of `DROP TABLE` differs based on table type:*
> * **Internal (Managed) Tables:** Deletes both schema and data from HDFS.
> * **External Tables:** Deletes only the schema; data in HDFS remains untouched.

---

## III. Data Querying (DQL) 📊

### General SELECT Statement Structure 🔍

-   **Full SELECT Statement Structure:**
```hiveql
SELECT [ * | DISTINCT col_name, col_name, ... ]
FROM table_name
[WHERE where_condition]
[GROUP BY col_list]
[HAVING having_condition]
[CLUSTER BY col_list | [DISTRIBUTE BY col_list] [SORT BY col_list]]
[LIMIT number];
```

### Common SELECT Examples 📈

-   **Select All Columns:**
```hiveql
SELECT * FROM table_name;
```
-   **Select Distinct Column Values:**
```hiveql
SELECT DISTINCT column_name FROM table_name;
```
-   **Limit Number of Rows:**
```hiveql
SELECT * FROM table_name LIMIT n_rows;
```
-   **Filter Data with WHERE Clause:**
```hiveql
SELECT * FROM table_name WHERE col_name = 'value';
```
-   **Aggregate with GROUP BY:**
```hiveql
SELECT col1, COUNT(*) FROM table_name GROUP BY col1;
```
-   **Filter Aggregated Results with HAVING:**
```hiveql
SELECT col1, COUNT(*) FROM table_name GROUP BY col1
HAVING COUNT(*) > 2;
```
-   **Order Results:**
```hiveql
SELECT * FROM table_name ORDER BY col_name [ASC|DESC];
```
-   **Perform a Join between Tables:** 🤝
```hiveql
SELECT col1, col2, col3, col4
FROM table1 t1
JOIN table2 t2
ON (t1.col5 = t2.col5);
```

---

## IV. Useful Hive Functions ➕➖

-   **Aggregate Functions:**
* `count(*)`: Count all rows.
* `count(DISTINCT expr)`: Count unique values.
* `sum(col)`: Sum of column values.
* `sum(DISTINCT col)`: Sum of unique column values.
* `avg(col)`: Average of column values.
* `avg(DISTINCT col)`: Average of unique column values.
* `min(col)`: Minimum value in column.
* `max(col)`: Maximum value in column.

-   **String Functions:**
* `concat(string A, string B,...)`: Concatenate strings.
* `substr(string A, int start)`: Get substring.
* `upper(string A)`: Convert to uppercase.
* `lower(string A)`: Convert to lowercase.
* `trim(string A)`: Trim whitespace.

-   **Numeric Functions:**
* `round(double a)`: Round to nearest integer.

-   **Date/Time Functions:**
* `to_date(string timestamp)`: Convert timestamp to date string.
* `year(string date)`: Extract year.
* `month(string date)`: Extract month.
* `day(string date)`: Extract day.
