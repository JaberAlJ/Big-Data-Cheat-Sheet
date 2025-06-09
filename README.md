# Big Data Commands Cheat Sheets

This resource is a comprehensive collection of commands and common operations for various Big Data technologies within the Hadoop ecosystem. It's designed to be a quick reference for developers, analysts, and anyone working with these powerful tools.

> ✍️ Written by: [*JaberAlJ*](https://github.com/JaberAlJ)

---

## 📂 Repository Structure

This repository is organized to make it easy to find the commands you need. Each core technology has its own dedicated directory under `Cheat Sheets/`, containing one or more Markdown files (`.md`) with detailed commands and explanations.

```bash
.
├── Cheat Sheets/
│   ├── HBase/
│   │   └── hbase.md
│   ├── HDFS/
│   │   └── hdfs.md
│   ├── Hive/
│   │   ├── hive_dynamic_partition.md
│   │   ├── hive_external_tables.md
│   │   ├── hive_internal_tables.md
│   │   ├── hive_static_partition.md
│   │   └── hive.md                         # Common Hive commands
│   ├── MapReduce/
│   │   ├── Employee Map Reducer/           # Example MapReduce
│   │   ├── Most Common Word Map Reducer/   # Example MapReduce
│   │   ├── Phone Map Reducer/              # Example MapReduce
│   │   ├── Store Map Reducer/              # Example MapReduce
│   │   └── Word Count Map Reducer/         # Example MapReduce
│   │   └── mapreduce.md                    # Core MapReduce commands
│   ├── Pig/
│   │   └── pig.md
│   └── Sqoop/
│       └── sqoop.md
├── .gitattributes
├── .gitignore
└── README.md
```

---

## 📝 Table of Contents

Navigate to the specific technology cheat sheets using the links below:

* ### [HBase Commands](Cheat%20Sheets/HBase/hbase.md) 🐘
    * Commands for interacting with Apache HBase, a NoSQL distributed database.

* ### [HDFS Commands](Cheat%20Sheets/HDFS/hdfs.md) ☁️
    * Commands for interacting with the Hadoop Distributed File System (HDFS).

* ### [Hive Commands 🐝](Cheat%20Sheets/Hive)
    * **[Common Hive Commands](Cheat%20Sheets/Hive/hive.md)**: Essential HiveQL and CLI commands applicable across various table types.
    * **[Hive Internal Tables](Cheat%20Sheets/Hive/hive_internal_tables.md)**: Commands for managing Hive's fully managed (internal) tables.
    * **[Hive External Tables](Cheat%20Sheets/Hive/hive_external_tables.md)**: Commands for managing external tables, where Hive manages only the schema.
    * **[Hive Static Partitioning](Cheat%20Sheets/Hive/hive_static_partition.md)**: Commands for loading data into explicitly defined partitions.
    * **[Hive Dynamic Partitioning](Cheat%20Sheets/Hive/hive_dynamic_partition.md)**: Commands for automatically creating partitions based on data values.

* ### [MapReduce Commands](Cheat%20Sheets/MapReduce/mapreduce.md) ⚙️
    * Commands for submitting, managing, and running MapReduce jobs, including streaming and YARN commands.

* ### [Pig Commands](Cheat%20Sheets/Pig/pig.md)
    * Commands for Apache Pig Latin scripting, for high-level data analysis.

* ### [Sqoop Commands](Cheat%20Sheets/Sqoop/sqoop.md) 🔗
    * Commands for importing and exporting data between Hadoop and relational databases like MySQL.

---

## 👋 Contribution

Contributions are always welcome! If you find any commands that are missing, incorrect, or could be improved, please feel free to:

1.  **Open an Issue**: Report a bug, suggest an enhancement, or ask a question.
2.  **Submit a Pull Request**: Make changes directly and submit them for review.
