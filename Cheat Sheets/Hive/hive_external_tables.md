# Hive External Tables Commands 🔗

This section details common commands for working with **External Tables** in Apache Hive. With external tables, Hive only manages the table's schema in its Metastore, while the actual data files reside externally in HDFS (or other storage). This means that **dropping an external table only removes the schema, leaving the data files intact** in their original location.

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

## II. Table Definition & Schema Changes ➕

### External Table Creation & Modification 🛠️

-   **Create an External Table:**
```hiveql
CREATE EXTERNAL TABLE table_name(
    col_name1 string,
    col_name2 int)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION '/path_of_data_dir';
```
*The `LOCATION` clause is crucial, pointing to the HDFS directory where your data already exists or where you will place it.*

-   **Describe Table Schema (Basic):**
```hiveql
DESCRIBE table_name;
```

-   **Describe Table Schema (Formatted Details):**
```hiveql
DESCRIBE FORMATTED table_name;
```

-   **Add a New Column to a Table:**
```hiveql
ALTER TABLE table_name ADD COLUMNS (new_col_name datatype);
```

-   **Drop an External Table:**
```hiveql
DROP TABLE table_name;
```

> [!IMPORTANT]
> *This command only removes the table definition from Hive. The actual data files in the specified `LOCATION` in HDFS will **remain untouched**.*

---

## III. Data Querying 📊

### General Query Structure & Examples 🔍

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
SELECT * FROM table_name WHERE col_name = '...';
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

---

## IV. Useful Hive Functions ➕➖

-   **Aggregate Functions:**
* `count(*)`: Count all rows.
* `count(DISTINCT expr)`: Count unique values.
* `sum(col)`: Sum of column values.
* `sum(DISTINCT col)`: Sum of unique column values.
* `avg(col)`: Average of column values.
* `avg(DISTINCT col)`: Average of unique column values.`min(col)`: Minimum value in column.
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