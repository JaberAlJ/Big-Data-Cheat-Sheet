# Sqoop Commands Cheat Sheet 🐘🔗

This section covers common commands for Apache Sqoop, a tool used for efficiently transferring bulk data between Hadoop and relational databases like MySQL.

---

## I. MySQL Basics 🗄️

Before using Sqoop to interact with MySQL, you'll often need to set up your database and tables.

-   **Connect to MySQL Shell:**
```bash
mysql -u root -p
```
*When prompted, enter your password (e.g., `cloudera`).*

-   **Show All Databases:**
```sql
SHOW DATABASES;
```

-   **Create a New Database:**
```sql
CREATE DATABASE dbName;
```

-   **Select a Database to Use:**
```sql
USE dbName;
```

### Table & Data Operations in MySQL ➕

-   **Create a Table in MySQL:**
```sql
CREATE TABLE tableName (
colName1 INT PRIMARY KEY,
colName2 VARCHAR(255)
);
```
*Example types: `INT`, `VARCHAR(length)`, `PRIMARY KEY`.*

-   **Insert Data into a MySQL Table:**
```sql
INSERT INTO tableName VALUES (1, 'value1');
INSERT INTO tableName (colName1, colName2) VALUES (2, 'value2');
```

-   **Select Data from a MySQL Table:**
```sql
SELECT * FROM tableName;
```

---

## II. Importing MySQL Data to Hive 🚀➡️📊

This process allows you to bring data from a MySQL table directly into a Hive table. Sqoop handles the schema conversion and data transfer.

1.  **Ensure you have a MySQL table with data.**
2.  **Create the corresponding table in Hive.**
> [!NOTE]
> *For Sqoop `hive-import` to work smoothly, you typically create an un-managed (external) Hive table, or let Sqoop create it. You don't usually specify `ROW FORMAT DELIMITED` explicitly when Sqoop is creating/managing it, as Sqoop handles the format.*
```hiveql
-- Example if Hive table already exists (Sqoop will append/overwrite)
-- CREATE TABLE hiveDB.tablename (id INT, name STRING);
```
3.  **Import the table from MySQL to Hive:**
```bash
sqoop import \
--connect jdbc:mysql://127.0.0.1:3306/mysqlDB \
--username root \
--password cloudera \
--table tableName \
--hive-import \
--hive-table hiveDB.tablename \
-m 1
```
* `--hive-import`: Tells Sqoop to import into Hive.*
* `--hive-table hiveDB.tablename`: Specifies the target Hive database and table name.*
* `-m 1`: Uses 1 mapper for the import (can be increased for parallelism).*

---

## III. Exporting Hive Data to MySQL 📊➡️🚀

This process allows you to take data from a Hive table and export it into an existing MySQL table.

1.  **Ensure you have a MySQL table with a compatible schema.**
2.  **Ensure you have a Hive table with data.**
> [!NOTE]
> *For `sqoop export`, the Hive table often needs to be configured with a delimited format so Sqoop knows how to parse the data.*
```hiveql
-- Example Hive table creation with delimiter
-- CREATE TABLE hiveDB.export_table (id INT, name STRING)
-- ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```
3.  **Export the table data from Hive into MySQL:**
```bash
sqoop export \
--connect jdbc:mysql://127.0.0.1:3306/mysqlDB \
--username root \
--password cloudera \
--table tableName \
--export-dir /user/hive/warehouse/hiveDB.db/tableName \
-m 1 \
--input-fields-terminated-by ','
```
* `--export-dir`: Specifies the HDFS directory where the Hive table data resides.*
* `--input-fields-terminated-by ','`: Tells Sqoop how to parse the fields in the input HDFS files.*

---

## IV. Importing MySQL Table to HDFS 📥☁️

This is used to bring data from a MySQL table directly into HDFS as flat files.

1.  **Ensure you have a MySQL table with data.**
2.  **Import the table data from MySQL to HDFS:**
```bash
sqoop import \
--connect jdbc:mysql://127.0.0.1:3306/mysqlDB \
--username root \
--password cloudera \
--table tableName \
-m 1
```
*Sqoop will create a directory in HDFS (by default, `/user/<your_username>/tableName`) and place the data there.*
-   **Verify data in HDFS:**
```bash
hdfs dfs -ls /user/cloudera/tableName
```
*Replace `/user/cloudera/tableName` with the actual path if different.*

---

## V. Exporting HDFS Data to MySQL 📤🗄️

This allows you to take data from flat files in HDFS and export it into an existing MySQL table.

1.  **Ensure you have a MySQL table with a compatible schema.**
2.  **Ensure you have data files in HDFS (e.g., `data.txt`)**
* *Example: `hdfs dfs -put local_data.txt /hdfsPath/data.txt`*
3.  **Export the data from HDFS into MySQL:**
```bash
sqoop export \
--connect jdbc:mysql://127.0.0.1:3306/mysqlDB \
--username root \
--password cloudera \
--table tableName \
--export-dir /hdfsPath/data.txt \
-m 1
```
