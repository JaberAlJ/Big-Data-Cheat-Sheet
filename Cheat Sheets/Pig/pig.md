# Pig Commands Cheat Sheet

This cheat sheet covers common commands and operations for Apache Pig Latin scripting. Pig provides a high-level language, Pig Latin, for expressing data analysis programs, and an infrastructure for evaluating these programs on large datasets.

---

## I. Pig Shell Basics 🚀

-   **Launch Pig Grunt Shell:**
```bash
pig
```
*You can also specify the execution mode: `pig -x local` for Local mode or `pig -x mapreduce` for MapReduce mode.*
-   **Clear Grunt Shell Screen:**
```piglatin
clear;
```
-   **Exit Grunt Shell:**
```piglatin
quit;
```
-   **Show Loaded Relations (Tables):**
```piglatin
show tables;
```
-   **View Command History:**
```piglatin
history;
```

---

## II. Data Loading & Inspection 📂

-   **Load Data from HDFS into a Relation:** 📥
> [!NOTE] 
> You can refer to columns by their `col_name` or by their `$index` (starting from 0).*
```piglatin
table_name0 = LOAD '/path/data.txt' USING PigStorage(',') AS (
col_name1:chararray,
col_name2:int
);
```

-   **Display Relation Content (for debugging/small datasets):** 🔍
```piglatin
dump table_name;
```
*This command executes the Pig Latin statement and displays results directly on the console.*

-   **Describe Relation Schema:** ℹ️
```piglatin
DESCRIBE table_name;
```

-   **Explain Execution Plan:** 🧠
```piglatin
EXPLAIN table_name;
```
*Use this to see the logical, physical, and MapReduce execution plans of your Pig script.*

-   **Illustrate Data Flow (with sample data):** 📊
```piglatin
ILLUSTRATE table_name;
```
*This provides a step-by-step visualization of how data transforms at each stage of your Pig script.*

-   **Store Relation Data to HDFS:** 📤
```piglatin
STORE table_name INTO '/path' USING PigStorage('\t');
```
> [!NOTE]
> The output path (`/path` in this example) **must not exist** before running the `STORE` command, or Pig will throw an error.*

---

## III. Data Transformation Operations ⚙️

-   **GROUP - Group Data by a Column:** 🤝
```piglatin
table_name2 = GROUP table_name BY col_name;
```

-   **FOREACH - Project or Transform Data:** 🔄
* **Select specific columns:**
```piglatin
table_name3 = FOREACH table_name GENERATE col_name1, col_name2;
```
* **Rename columns during projection:**
```piglatin
table_name3 = FOREACH table_name GENERATE col_name1 AS new_col_name, col_name2;
```

-   **FILTER - Select Rows based on Condition:** 🔎
*Common operators: `>`, `<`, `>=`, `<=`, `==`, `!=`*
```piglatin
table_name4 = FILTER table_name BY col_name > 50;
```

-   **LIMIT - Restrict Number of Rows:** 🎯
```piglatin
table_name5 = LIMIT table_name 5;
```

-   **ORDER - Sort Data:** ⬆️⬇️
*Specify sort direction: `ASC` (Ascending) or `DESC` (Descending)*
```piglatin
table_name6 = ORDER table_name BY col_name DESC;
```

---

## IV. Combined Operations 🧩

-   **FILTER & FOREACH:**
```piglatin
table_name7 = FILTER (FOREACH table_name GENERATE col_name, col_name1) BY col_name1 > 85;
```

-   **GROUP & FOREACH:**
```piglatin
table_name8 = GROUP (FOREACH table_name GENERATE col_name, col_name1) BY col_name1;
```

-   **ORDER & FOREACH:**
```piglatin
table_name9 = ORDER (FOREACH table_name GENERATE col_name, col_name1) BY col_name1 DESC;
```

---

## V. Grouping with Aggregate Functions 📈

When you `GROUP` data, the result is a relation where each tuple contains the grouping key and a bag of all tuples that belong to that group. You then use `FOREACH ... GENERATE` with aggregate functions on this bag.

-   **Describe Grouped Relation Schema:**
```piglatin
DESCRIBE table_name2;
```
*Example Schema:* `table_name2: {group: datatype, table_name: {(col_name1: datatype, col_name2: datatype)}}`

-   **Perform Aggregations (MAX, MIN, SUM, AVG, COUNT):**
```piglatin
table_name10 = FOREACH table_name2 GENERATE group, MAX(table_name.col_name2);
```
```piglatin
table_name10 = FOREACH table_name2 GENERATE group, MIN(table_name.col_name2);
```
```piglatin
table_name10 = FOREACH table_name2 GENERATE group, SUM(table_name.col_name2);
```
```piglatin
table_name10 = FOREACH table_name2 GENERATE group, AVG(table_name.col_name2) AS new_col_name_avg, COUNT(table_name) AS new_col_name_count;
```

---

## VI. Multi-Relation Operations

-   **COGROUP - Group Data from Multiple Relations:**
```piglatin
table_name11 = COGROUP table_name0 BY col_name1, table_name00 BY col_name1;
```
*This operation groups records from two or more relations based on common fields, allowing for combined analysis.*
