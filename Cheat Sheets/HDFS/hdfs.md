# HDFS Commands Cheat Sheet ✨

This section covers common commands for interacting with the Hadoop Distributed File System (HDFS).

---

## Basic HDFS Operations 📁

- **Switch User (Linux/Cloudera environment):**
```bash
$ su cloudera
```

- **Clear Terminal Screen:** 🧹
```bash
$ clear
```

- **List directory contents:** 📜
```bash
$ hdfs dfs -ls /
```

- **Create a directory:** ➕📁
```bash
$ hdfs dfs -mkdir /folderName 
```

- **Create an empty file:** 📝
```bash
$ hdfs dfs -touchz /folderName/fileName.ext
```

- **Check disk usage of a file/directory:** 📊
```bash
$ hdfs dfs -du -s /folderName/fileName.ext
```

- **Append to a file (input from stdin):** ✍️
```bash
$ hdfs dfs -appendToFile - /folderName/fileName.ext
```
*(After running this, type your content and press Ctrl+D to save.)*

- **View file content:** 📖
```bash
$ hdfs dfs -cat /folderName/fileName.ext
```

- **Copy a file within HDFS:** 📋
```bash
$ hdfs dfs -cp /folderName/fileName.ext /folderName
```

- **Move/Rename a file within HDFS:** 🚚
```bash
$ hdfs dfs -mv /folderName/fileName.ext /folderName
```

- **Remove an empty directory:** ❌📁
```bash
$ hdfs dfs -rmdir /folderName
```

- **Remove a file:** 🗑️
```bash
$ hdfs dfs -rm /folderName/fileName.ext
```

- **Remove a directory and its contents recursively:**
```bash
$ hdfs dfs -rm -r /folderName/fileName.ext
```

## Local File System (LFS) to HDFS & Vice Versa ↔️

- **Copy from Local File System to HDFS:** ⬆️☁️
```bash
$ hdfs dfs -copyFromLocal /home/cloudera/LFSfileName.ext /HDFSfolderName
```

- **Put file from Local File System to HDFS (alias for copyFromLocal):** 📤☁️
```bash
$ hdfs dfs -put /home/cloudera/LFSfileName.ext /HDFSfolderName
```

- **Copy from HDFS to Local File System:** ⬇️🖥️
```bash
$ hdfs dfs -copyToLocal /folderName/HDFSfileName.ext /home/cloudera/LFSfolderName
```

- **Get file from HDFS to Local File System (alias for copyToLocal):** 📥🖥️
```bash
$ hdfs dfs -get /folderName/HDFSfileName.ext /home/cloudera/LFSfolderName
```

- **Move from Local File System to HDFS (deletes local file):** ➡️☁️
```bash
$ hdfs dfs -moveFromLocal /home/cloudera/_LFSfileName_.ext /_HDFSfolderName_
```

- **Move from HDFS to Local File System (deletes HDFS file):** ⬅️🖥️
```bash
$ hdfs dfs -moveToLocal /folderName/HDFSfileName.ext /home/cloudera/LFSfolderName
```

## Advanced HDFS Operations & Utilities ⚙️

- **Display the last kilobyte of a file:** 🔚
```bash
$ hdfs dfs -tail /folderName/fileName.ext
```
(You need to specify a file path)

- **Get help for HDFS commands:**
```bash
$ hdfs dfs -help ❓
$ hdfs dfs -help [command_name]
```
(e.g., `hdfs dfs -help ls`)

- **Get file/directory status information (e.g., replication factor):** ℹ️
```bash
$ hdfs dfs -stat %r /folderName/HDFSfileName.ext
```

- **Change the replication factor of a file/directory:** 🔄
```bash
$ hdfs dfs -setrep -R NumberOfRepFac /folderName/HDFSfileName.ext
```

- **Display free and used space on the filesystem:** 💾
```bash
$ hdfs dfs -df -h /folderName/HDFSfileName.ext
```
(You can also use just `/` for the whole system) 

- **Change ownership:** 👥
```bash
hdfs dfs -chown -R user:group /hdfs/path
```

- **Change permissions:** 🔑
```bash
hdfs dfs -chmod -R 755 /hdfs/path
```

- **Display HDFS file system health:** 🩺
```bash
hdfs dfsadmin -report
```