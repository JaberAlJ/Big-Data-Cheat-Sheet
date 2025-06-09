# Hive Static Partitioning Commands ➡️📂

This section covers commands for creating and loading data into Hive tables using **Static Partitioning**. With static partitioning, you explicitly define the partition column value(s) within your `LOAD DATA` or `INSERT` statements. This method is handy when you already know the specific partition values for the data you're adding.

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

-   **Create a Basic Partitioned Table:**
```hiveql
CREATE TABLE table_name(
    col1_name string,
    col2_name int)
PARTITIONED BY (col3_name string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

-   **Create a Partitioned, Clustered, and Sorted Table (with Bucketing):**
```hiveql
CREATE TABLE table_name( col1 type, col2 type)
PARTITIONED BY ( col3 type)
CLUSTERED BY ( col2 )
SORTED BY ( col2 DESC)
INTO 2 BUCKETS
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

-   **Describe Table Schema:**
```hiveql
DESCRIBE table_name;
```

-   **Show Partitions for a Table:**
```hiveql
SHOW PARTITIONS db.table_name;
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
> *For internal tables (the default for `CREATE TABLE`), this deletes both the schema and the data!*

---

## III. Data Loading & Querying 📊

### Data Loading into Static Partitions 📥

-   **Load Data into Specific Static Partitions:**
```hiveql
LOAD DATA [LOCAL] INPATH '/home/cloudera/data1.txt' INTO TABLE table_name
PARTITION (col3_name = 'value1');
```
```hiveql
LOAD DATA [LOCAL] INPATH '/home/cloudera/data2.txt' INTO TABLE table_name
PARTITION (col3_name = 'value2');
```
```hiveql
LOAD DATA [LOCAL] INPATH '/home/cloudera/data3.txt' INTO TABLE table_name
PARTITION (col3_name = 'value3');
```
*Hive will create directories like `col3_name=value1` under the table's HDFS path and move the data there.*

-   **Insert Specific Values into Table (if not partitioned, or to an existing partition if column matches):**
```hiveql
INSERT INTO table_name VALUES (value1, value2, ...);
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