# Hive Dynamic Partitioning Commands 🧙‍♂️📂

This section covers commands for using **Dynamic Partitioning** in Apache Hive. Dynamic partitioning automatically determines the partition column values based on the data being loaded or inserted. This is incredibly efficient for large datasets, as it eliminates the need to manually specify each partition value.

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

## II. Hive Configuration for Dynamic Partitioning ⚙️

Before performing dynamic partition inserts, you need to enable it and set the mode.

### Dynamic Partitioning Settings 🚦

-   **Enable Dynamic Partitioning:**
```hiveql
SET hive.exec.dynamic.partition = true;
```
-   **Set Dynamic Partition Mode to Nonstrict:** (Allows all partitions to be dynamic, without requiring a static partition.)
```hiveql
SET hive.exec.dynamic.partition.mode = nonstrict;
```
-   **Set Max Dynamic Partitions (Optional):** (Limits the total number of partitions created in a single command.)
```hiveql
SET hive.exec.max.dynamic.partitions=100;
```
-   **Set Max Dynamic Partitions Per Node (Optional):** (Limits partitions created per task node.)
```hiveql
SET hive.exec.max.dynamic.partitions.pernode=100;
```

---

## III. Table Definition & Schema Changes ➕

### Table Creation & Modification 🛠️

-   **Create a Staging/Source Table (non-partitioned, if needed as input):**
```hiveql
CREATE TABLE table_name(
    col1_name string,
    col2_name int)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

-   **Create a Partitioned Table (Destination for Dynamic Partitions):**
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

## IV. Data Loading & Dynamic Partitioning 📊

### Data Loading (into a non-partitioned source table, if applicable) 📥

-   **Load Data into a Non-Partitioned Source Table:**
```hiveql
LOAD DATA [LOCAL] INPATH '/home/cloudera/data.txt' INTO TABLE table_name;
```

### Insert into Dynamic Partitions ➡️

-   **Insert Data into a Dynamically Partitioned Table:**
*The partition column (`col3_name`) must be the **last column** in your `SELECT` statement.*
```hiveql
INSERT INTO TABLE dynamic_partition_table_name PARTITION(col3_name)
SELECT col1_name, col2_name, col3_value_from_source_table_or_expression
FROM source_table_name;
```
*Hive will automatically create partitions based on the values in `col3_value_from_source_table_or_expression`.*

---

## V. General Querying & Functions 🔍

### General Query Structure & Examples 📈

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

## VI. Useful Hive Functions ➕➖

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