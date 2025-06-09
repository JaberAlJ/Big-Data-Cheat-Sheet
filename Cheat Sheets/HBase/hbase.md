# HBase Commands Cheat Sheet 🐘

This section covers common commands for interacting with Apache HBase, a NoSQL distributed database, primarily through its shell.

---

## I. HBase Shell & General Commands 🚀

-   **Launch HBase Shell:**
```bash
hbase shell
```
-   **Exit HBase Shell:**
```hbaseql
quit
```
-   **Clear Shell Screen:**
```hbaseql
ctrl + L
```
-   **Check HBase Cluster Status:** 🩺
```hbaseql
status
```
-   **Display HBase Version:** 🏷️
```hbaseql
version
```
-   **Show Current User:** 👤
```hbaseql
whoami
```

---

## II. Table Management 📊

-   **List All Tables:** 📜
```hbaseql
list
```

-   **Create a Table with Column Families:** ➕
```hbaseql
create 'tableName', 'colFamily1', 'colFamily2'
```

-   **Disable a Table:** 🚫
```hbaseql
disable 'tableName'
```

-   **Enable a Table:** ✅
```hbaseql
enable 'tableName'
```

-   **Describe Table Schema:** ℹ️
```hbaseql
describe 'tableName'
```

-   **Count Rows in a Table:** 🔢
```hbaseql
count 'tableName'
```

-   **Drop a Table:** 🗑️
> [!NOTE]
> *A table must be **disabled** before it can be dropped.*

```hbaseql
drop 'tableName'
```

---

## III. Data Displaying & Retrieval 🔍

-   **Scan (Retrieve All Rows/Range):**
```hbaseql
scan 'tableName'
```

-   **Get a Single Row by Key:**
```hbaseql
get 'tableName', 'rowKey'
```

-   **Get Specific Column from a Row:**
```hbaseql
get 'tableName', 'rowKey', {COLUMN=>'colFamily:columnName'}
```

-   **Get Multiple Specific Columns from a Row:**
```hbaseql
get 'tableName', 'rowKey', {COLUMN=>['colFamily:columnName1', 'colFamily:columnName2']}
```

---

## IV. Column Family Operations ⚙️

-   **Alter Table (Add/Modify Column Family):** ✏️
```hbaseql
alter 'tableName', {NAME=>'newColFamily'}
```
*To modify properties, add them within the curly braces, e.g., `{NAME=>'colFamily', VERSIONS=>5}`*

-   **Alter Table (Delete Column Family):** ❌
```hbaseql
alter 'tableName', 'delete'=>'colFamily'
```

---

## V. Data Insertion & Updating ✍️

-   **Put (Insert or Update a Cell Value):**
```hbaseql
put 'tableName', 'rowKey', 'colFamily:columnName', 'value'
```

---

## VI. Deleting Rows & Values 🗑️

-   **Delete All Values in a Row:**
```hbaseql
deleteall 'tableName', 'rowKey'
```

-   **Delete a Specific Cell Value in a Row:**
```hbaseql
delete 'tableName', 'rowKey', 'colFamily:columnName'
```

---

## VII. Data Loading from HDFS to HBase ☁️➡️📊

This method uses the `ImportTsv` MapReduce job to load delimited data from HDFS into an HBase table.

1.  **Create a table in HBase with the required Column Families:**
```hbaseql
create 'myDataTable', 'dataCF'
```
2.  **Create a text file (e.g., `data.txt`) in your Local File System.**
*Example `data.txt` content (comma-separated):*
`row1,value1,valueA`
`row2,value2,valueB`
3.  **Copy the file to HDFS:**
```bash
hdfs dfs -put /home/cloudera/data.txt /user/hadoop/hbase_import/
```
4.  **Load the data to the HBase table using `ImportTsv`:**
```bash
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=, -Dimporttsv.columns=HBASE_ROW_KEY,dataCF:col1,dataCF:col2 myDataTable /user/hadoop/hbase_import/data.txt
```
*`-Dimporttsv.separator=,`: Specifies comma as the delimiter.*
*`-Dimporttsv.columns=HBASE_ROW_KEY,colFamily:columnName,...`: Maps input fields to HBase row key and columns.*
5.  **Check the HBase table to confirm data was loaded:** 🔍
```hbaseql
scan 'myDataTable'
```

---

## VIII. Hive & HBase Integration 🤝

You can integrate Hive with HBase, allowing you to query HBase tables using HiveQL.

1.  **Create a Hive External Table mapped to an HBase Table (run in Hive shell):**
```hiveql
CREATE EXTERNAL TABLE tableName(keyCol colType, colName1 colType, colName2 colType)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES (
"hbase.columns.mapping"=":key,colFamily1:columnName1,colFamily2:columnName2"
)
TBLPROPERTIES ("hbase.table.name"="hbaseTableName");
```
*`:key` maps to the HBase row key.*
*`colFamily:columnName` maps to the respective HBase column.*

2.  **Check if the table was created in both Hive and HBase:**
* **Hive:**
```hiveql
show tables;
```
* **HBase:**
```hbaseql
list
```

---

## IX. Versioning ⏳

HBase supports cell versioning, allowing you to store multiple versions of a value for a given cell.

-   **Alter Column Family to Store Multiple Versions:**
```hbaseql
alter 'tableName', NAME=>'colFamily', VERSIONS=>3
```
*This sets the `colFamily` to store up to 3 versions of each cell's value.*

-   **Get Specific Number of Versions for a Column:**
```hbaseql
get 'tableName', 'rowKey', {COLUMN=>'colFamily:columnName', VERSIONS=>2}
```
*This retrieves the 2 most recent versions of the specified column's value.*
