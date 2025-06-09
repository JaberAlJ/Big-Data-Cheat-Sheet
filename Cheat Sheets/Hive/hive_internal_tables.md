# Hive Internal Tables Commands ✨

This section covers common commands for interacting with **Internal (Managed) Tables** in Apache Hive. Remember, when you drop an internal table, Hive deletes both its schema and the actual data stored in HDFS.

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

### Table Creation & Modification 🛠️

-   **Create an Internal Table:**
```hiveql
CREATE TABLE table_name(
col_name1 string,
col_name2 int)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```
-   **Describe Table Schema:**
```hiveql
DESCRIBE table_name;
```
-   **Add a New Column to a Table:**
```hiveql
ALTER TABLE table_name ADD COLUMNS (new_col_name datatype);
```
-   **Drop a Table:**
```hiveql
DROP TABLE table_name;
```

> [!CAUTION]
> *For internal tables, this deletes both the schema and the data!*

---

## III. Data Loading & Querying 📊

### Data Loading & Insertion 📥

-   **Load Data into Table (from Local FS):**
```hiveql
LOAD DATA LOCAL INPATH '/home/cloudera/data.txt' INTO TABLE table_name;
```
-   **Insert Specific Values into Table:**
```hiveql
INSERT INTO table_name VALUES (value1, value2, ...);
```

### Joins 🤝

-   **Perform a Join between Tables:**
```hiveql
SELECT col1, col2, col3, col4
FROM table1 t1
JOIN table2 t2
ON (t1.col5 = t2.col5);
```

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