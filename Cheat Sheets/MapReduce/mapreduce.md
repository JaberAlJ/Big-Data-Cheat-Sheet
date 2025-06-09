# MapReduce Commands Cheat Sheet ✨

This section covers common commands for submitting, managing, and running MapReduce jobs.

---

## Submitting Jobs 🚀

-   **Submit a JAR job:**
```bash
hadoop jar /path/to/your/job.jar com.yourcompany.YourDriverClass /input/path /output/path
```

-   **Submit a generic Hadoop command (e.g., streaming):**
```bash
hadoop [command]
```

---

## Job Management 📊

-   **List all running jobs (Deprecated in YARN):**
```bash
mapred job -list
```

-   **Kill a running job (Deprecated in YARN):**
```bash
mapred job -kill job_id
```

---

## Run MapReduce on HDFS ☁️

This section outlines the steps to prepare input and run a streaming MapReduce job on HDFS.

1.  **Create an input file in the Local File System (LFS):** 📝
```bash
cat >> fileName.txt
```
OR
```bash
nano fileName.txt
```

2.  **Run the file on LFS (for testing/understanding):** 🧪
* **Mapper only:**
```bash
cat fileName.txt | ./mapred/mapperFile.py
```
* **Mapper and Sort:**
```bash
cat fileName.txt | python mapred/mapperFile.py | sort
```
* **Mapper, Sort, and Reducer:**
```bash
cat fileName.txt | ./mapred/mapperFile.py | sort | ./mapred/reducerFile.py
```

3.  **Prepare HDFS for input:** 📂
* **a) Create an input directory in HDFS:**
```bash
hdfs dfs -mkdir /_folderName_ /inputFolder
```
* **b) Create an input file in HDFS and append content:**
```bash
hdfs dfs -touchz /_folderName_ /inputFolder/inputFile.txt
```
```bash
hdfs dfs -appendToFile - /_folderName_ /inputFolder/inputFile.txt
```
*(Type your content and press `Ctrl+D` to save.)*

4.  **Run the MapReduce job on HDFS:** 🏃‍♀️
* First, navigate to your MapReduce script directory:
```bash
cd mapred
```
* Then, execute the streaming job:
```bash
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-files mapperFile.py,reducerFile.py \
-mapper mapperFile.py \
-reducer reducerFile.py \
-input /_folderName_/inputFolder/inputFile.txt \
-output /_folderName_/outputFolder
```

5.  **Check the MapReduce output:** 🔍
* **View specific part file:**
```bash
hdfs dfs -cat /_folderName_/outputFolder/part-00000
```
* **View all part files (if multiple):**
```bash
hdfs dfs -cat /_folderName_/outputFolder/part-0*
```

> [!NOTE]
> If you encounter an error like "output already exists", you need to remove the previous output directory before re-running the job: 🗑️

```bash
hdfs dfs -rm -r /_folderName_/outputFolder
```

---

## Run MapReduce on LFS (Local File System) 🖥️

This section describes how to run a MapReduce job directly on your local Linux file system using Python scripts and piping.

1.  **Create a directory for your MapReduce scripts:**
```bash
mkdir mapred
```
*Current directory:* `/home/cloudera`

2.  **Change into the newly created directory:**
```bash
cd mapred
```
*Current directory:* `/home/cloudera/mapred`

3.  **Copy your Python mapper and reducer programs** into this `mapred` folder. You can use tools like FileZilla from Windows or download them directly in Linux. ⬇️

4.  **Give executable authority to your Python programs:** ✨
```bash
chmod a+x *.py
```

5.  **Run the Mapper, Sort, and Reducer in a pipeline:** ➡️
```bash
cat _fileName_.txt | ./mapperFile.py | sort | ./reducerFile.py
```