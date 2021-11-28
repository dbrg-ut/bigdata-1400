#### Enter the Name Node

to run this command , in command line execute the following command to enter the **Name Node** :  

```bash
docker exec -it namenode bash
```



#### HDFS Commands  - Part 1

```bash
$ cd 
$ hadoop version
Hadoop 3.2.1
Source code repository https://gitbox.apache.org/repos/asf/hadoop.git -r b3cbbb467e22ea829b3808f4b7b01d07e0bf3842
Compiled by rohithsharmaks on 2019-09-10T15:56Z
Compiled with protoc 2.5.0
From source with checksum 776eaf9eee9c0ffc370bcbc1888737
This command was run using /opt/hadoop-3.2.1/share/hadoop/common/hadoop-common-3.2.1.jar

$ hadoop fs -mkdir /books
$ hadoop fs -mkdir -p /data/incomes
$ hadoop fs –ls /
Found 3 items
drwxr-xr-x   - root supergroup          0 2021-01-01 18:28 /books
drwxr-xr-x   - root supergroup          0 2021-01-01 18:29 /data
drwxr-xr-x   - root supergroup          0 2021-01-01 17:29 /rmstate

$ hadoop fs –ls -R /data
drwxr-xr-x   - root supergroup          0 2021-01-01 18:29 /data/incomes

$ hadoop fs -put /data/income.csv /data/incomes
2021-01-01 18:43:01,577 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
$ hadoop fs -ls /data/incomes
Found 1 items
-rw-r--r--   1 root supergroup    5326368 2021-01-01 18:43 /data/incomes/income.csv

$ hadoop fs -get /data/incomes/income.csv .

$ ls -lh
total 5.1M
-rw-r--r-- 1 root root 5.1M Jan  1 18:47 income.csv

$ hadoop fs -copyFromLocal  /data/war-and-peace-tolstoy.txt  /books
$ fs -ls -h /books
Found 1 items
-rw-r--r--   1 root supergroup      3.2 M 2021-01-01 18:55 /books/war-and-peace-tolstoy.txt

$ hadoop fs -copyToLocal  /books/war-and-peace-tolstoy.txt  .
$ ls -lh
total 8.3M
-rw-r--r-- 1 root root 5.1M Jan  1 18:54 income.csv
-rw-r--r-- 1 root root 3.2M Jan  1 18:57 war-and-peace-tolstoy.txt

$ hadoop fs -cat /books/war-and-peace-tolstoy.txt
﻿
The Project Gutenberg EBook of War and Peace, by Leo Tolstoy


BOOK ONE: 1805
....
$ hadoop fs -head /data/incomes/income.csv
2021-01-01 19:03:33,312 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
age,workclass,fnlwgt,education,educational-num,marital-status,occupation,relationship,race,gender,capital-gain,capital-loss,hours-per-week,native-country,income
25,Private,226802,11th,7,Never-married,Machine-op-inspct,Own-child,Black,Male,0,0,40,United-States,<=50K

$ hadoop fs -tail /data/incomes/income.csv
2021-01-01 19:15:27,206 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
Eskimo,Male,0,0,40,United-States,<=50K
43,Private,84661,Assoc-voc,11,Married-civ-spouse,Sales,Husband,White,Male,0,0,45,United-States,<=50K
32,Private,116138,Masters,14,Never-married,Tech-support,Not-in-family,Asian-Pac-Islander,Male,0,0,11,Taiwan,<=50K
53,Private,321865,Masters,14,Married-civ-spouse,Exec-managerial,Husband,White,Male,0,0,40,United-States,>50K

$ hadoop fs -cat /data/incomes/income.csv | wc -l
2021-01-01 19:16:23,365 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
48842

$ hadoop fs -mv /data/incomes/income.csv /data/incomes/income-us.csv
$ hadoop fs -ls -R /data
drwxr-xr-x   - root supergroup          0 2021-01-01 19:18 /data/incomes
-rw-r--r--   1 root supergroup    5326368 2021-01-01 18:43 /data/incomes/income-us.csv

$ hadoop fs -cp /data/incomes/income-us.csv /data/incomes/income.csv
hadoop fs -ls -R /data
drwxr-xr-x   - root supergroup          0 2021-01-01 19:22 /data/incomes
-rw-r--r--   1 root supergroup    5326368 2021-01-01 18:43 /data/incomes/income-us.csv
-rw-r--r--   1 root supergroup    5326368 2021-01-01 19:22 /data/incomes/income.csv

$ hadoop fs -rm /data/incomes/income.csv
Deleted /data/incomes/income.csv
```



#### HDFS Commands  - Part 2

```bash
$ cd 
$ hdfs dfs -ls -R /data
drwxr-xr-x   - root supergroup          0 2021-01-01 19:25 /data/incomes
-rw-r--r--   1 root supergroup    5326368 2021-01-01 18:43 /data/incomes/income-us.csv

```

Note that **hdfs dfs** and **hadoop fs** commands become synonymous if the filing system which is used is **HDFS**.

```bash
$ cp /data/income.csv /data/income2.csv
$ hadoop fs -mkdir /tmp
$ hadoop fs -moveFromLocal /data/income2.csv /tmp
$ ls -lh /data/
total 8.3M
-rwxrwxrwx 1 root root 5.1M Jan  1 16:21 income.csv
-rwxrwxrwx 1 root root 3.2M Jan  1 16:32 war-and-peace-tolstoy.txt

$ hadoop fs -ls -h /tmp
Found 1 items
-rw-r--r--   1 root supergroup      5.1 M 2021-01-01 19:53 /tmp/income2.csv

$ hadoop fs -moveToLocal /tmp/income2.csv .
moveToLocal: Option '-moveToLocal' is not implemented yet.

$hadoop fs -expunge

$ HADOOP_USER_NAME=hdfs hadoop dfs -put /data/income.csv /
$ hadoop fs -ls -h /
-rw-r--r--   1 hdfs    supergroup      5.1 M 2021-01-01 20:23 /income.csv

$ hadoop fs -chmod ug+x /income.csv
$ hadoop fs -ls -h /
-rwxr-xr--   1 hdfs    supergroup      5.1 M 2021-01-01 20:23 /income.csv

$ hadoop fs -chown  ali:hduser /income.csv
$ hadoop fs -ls -h /
-rwxr-xr--   1 ali     hduser          5.1 M 2021-01-01 20:23 /income.csv

$ hadoop fs -chgrp  test /income.csv
$ hadoop fs -ls -h /
-rwxr-xr--   1 ali     test            5.1 M 2021-01-01 20:23 /income.csv

$ hadoop fs -setrep 2 /income.csv
Replication 2 set: /income.csv
$ hdfs fsck /income.csv -files -blocks -locations
Connecting to namenode via http://namenode:9870/fsck?ugi=root&files=1&blocks=1&locations=1&path=%2Fincome.csv
FSCK started by root (auth:SIMPLE) from /172.18.0.6 for path /income.csv at Fri Jan 01 20:37:59 UTC 2021
/income.csv 5326368 bytes, replicated: replication=2, 1 block(s):  Under replicated BP-195919011-172.18.0.6-1609522134589:blk_1073741847_1023. Target Replicas is 2 but found 1 live replica(s), 0 decommissioned replica(s), 0 decommissioning replica(s).
.....
 
```



##### Add a Data Node to the cluster

stop the docker containers --> `Ctrl+c`

run docker-compose with second file : `docker-compose -f docker-compose2.yml`

```bash
### go to the name node with new id
$ hdfs fsck /income.csv -files -blocks -locations
Connecting to namenode via http://namenode:9870/fsck?ugi=root&files=1&blocks=1&locations=1&path=%2Fincome.csv
FSCK started by root (auth:SIMPLE) from /172.19.0.8 for path /income.csv at Fri Jan 01 20:47:31 UTC 2021
/income.csv 5326368 bytes, replicated: replication=2, 1 block(s):  OK
0. BP-195919011-172.18.0.6-1609522134589:blk_1073741847_1023 len=5326368 Live_repl=2  [DatanodeInfoWithStorage[172.19.0.3:9866,DS-efe255d1-afb3-4692-b3c7-21d9bb7651bf,DISK], DatanodeInfoWithStorage[172.19.0.6:9866,DS-3ec88224-b4fd-4246-be53-4750c0f5a5b8,DISK]]

$ hadoop fs -du -s -h /data
5.1 M  5.1 M  /data

$ hadoop fs -df  -h
Filesystem               Size    Used  Available  Use%
hdfs://namenode:9000  502.0 G  24.0 M    468.2 G    0%

```



#### HDFS Commands  - Part 3

```bash
$ cd 
$ hadoop fs -setrep 1 /income.csv
#### set rep to 1 to prevent going datanode to safemode
$ hdfs dfs -ls -R /data
drwxr-xr-x   - root supergroup          0 2021-01-01 19:25 /data/incomes
-rw-r--r--   1 root supergroup    5326368 2021-01-01 18:43 /data/incomes/income-us.csv
$ hadoop fs -touchz /temp.txt
root@namenode:/# hadoop fs -ls /temp.txt
-rw-r--r--   1 root supergroup          0 2021-01-02 05:50 /temp.txt
$ hadoop fs -touch /temp2.txt
$ hadoop fs -ls /temp2.txt
-rw-r--r--   1 root supergroup          0 2021-01-02 05:51 /temp2.txt


$ hadoop fs -test -e /temp2.txt
$ hadoop fs -test -e /temp2.txt && echo "File Exist"
File Exist

$ hdfs dfs -test -z /temp2.txt
$ hadoop fs -test -z /temp2.txt && echo Hi

$ hdfs dfs -test -d /temp2.txt
```

| **Options** | **Description**                                              |
| ----------- | ------------------------------------------------------------ |
| **-d**      | Check whether the path given by the user is a directory or not, return 0 if it is a directory. |
| **-e**      | Check whether the path given by the user exists or not, return 0 if the path exists. |
| **-f**      | Check whether the path given by the user is a file or not, return 0 if it is a file. |
| **-s**      | Check if the path is not empty, return 0 if a path is not empty. |
| **-r**      | return 0 if the path exists and read permission is granted   |
| **-w**      | return 0 if the path exists and write permission is granted  |
| **-z**      | Checks whether the file size is 0 byte or not, return 0 if the file is of 0 bytes. |



```bash
$ hadoop fs -text /books/war-and-peace-tolstoy.txt

...
As in the question of astronomy then, so in the question of history
now, the whole difference of opinion is based on the recognition or
nonrecognition of something absolute, serving as the measure of visible
phenomena. In astronomy it was the immovability of the earth, in history
it is the independence of personality—free will.
.....

$ hadoop fs -stat %a /books/war-and-peace-tolstoy.txt
644
$ hadoop fs -stat %y /books/war-and-peace-tolstoy.txt
2021-01-01 18:55:33
```

**Stat Formats:**

**%b –**  file size in bytes
 **%g –**  group name of owner
 **%n –**  file name
 **%o –**  block size
 **%r –**   replication
 **%u –**  user name of owner
 **%y –**  modification date



```bash
$ hadoop fs -usage stat
Usage: hadoop fs [generic options] -stat [format] <path> ...
$ hadoop fs -usage ls
Usage: hadoop fs [generic options] -ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [-e] [<path> ...]


$ hadoop fs -help ls
-ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [-e] [<path> ...] :
  List the contents that match the specified file pattern. If path is not
  specified, the contents of /user/<currentUser> will be listed. For a directory a
  list of its direct children is returned (unless -d option is specified).

  Directory entries are of the form:
        permissions - userId groupId sizeOfDirectory(in bytes)
  modificationDate(yyyy-MM-dd HH:mm) directoryName

  and file entries are of the form:
        permissions numberOfReplicas userId groupId sizeOfFile(in bytes)
  modificationDate(yyyy-MM-dd HH:mm) fileName

    -C  Display the paths of files and directories only.
    -d  Directories are listed as plain files.
    -h  Formats the sizes of files in a human-readable fashion
        rather than a number of bytes.
    -q  Print ? instead of non-printable characters.
    -R  Recursively list the contents of directories.
    -t  Sort files by modification time (most recent first).
    -S  Sort files by size.
    -r  Reverse the order of the sort.
    -u  Use time of last access instead of modification for
        display and sorting.
    -e  Display the erasure coding policy of files and directories.
    
    
$ echo "hello world" | hadoop fs -put - /hello_world.txt
$ echo "bye" | hadoop fs -put - /bye.txt
$ hadoop fs -ls /
Found 10 items
drwxr-xr-x   - root    supergroup          0 2021-01-01 18:55 /books
-rw-r--r--   1 root    supergroup          4 2021-01-02 06:12 /bye.txt
drwxr-xr-x   - root    supergroup          0 2021-01-01 18:29 /data
-rw-r--r--   1 root    supergroup         12 2021-01-02 06:12 /hello_world.txt
...
 
$ echo "Bye " > bye.txt
$ echo "Hi again " > hi.txt

$ hadoop fs -appendToFile hi.txt bye.txt /hello_world.txt
$ hadoop fs -cat /hello_world.txt
hello world
Hi again
Bye

#hadoop fs -appendToFile <localsrc> <dest>
$  echo "Hi 2" | hadoop  fs -appendToFile - t.txt 
$ hadoop fs -ls  /t2.txt
ls: `/t2.txt': No such file or directory

$ hadoop fs -ls  /user/root/t2.txt
-rw-r--r--   1 root supergroup          8 2021-01-02 06:40 /user/root/t2.txt

$ hadoop fs -count -v -h /
   DIR_COUNT   FILE_COUNT       CONTENT_SIZE PATHNAME
          13           29             18.4 M /
```

**Count Options:**
 **-q** – shows quotas(quota is the hard limit on the number of names and amount of space used for individual directories)
 **-u **-  it limits output to show quotas and usage only
 **-h** – shows sizes in a human-readable format
 **-v** – shows header line



```bash
$ hadoop fs -find / -name hello* 
/hello_world.txt
/user/root/hello_world.txt

$ hadoop fs -getmerge /t.txt /hello_world.txt /bye.txt merge.txt
$ cat merge.txt
HIIIIII
hello world
Hi again
Hi again
Bye
bye
```



##### Some Admin Command

```bash
$ hdfs dfsadmin -safemode get
Safe mode is ON
root@namenode:/# 
$ hdfs dfsadmin -safemode leave
Safe mode is OFF
$ hdfs dfsadmin -report
Configured Capacity: 269490393088 (250.98 GB)
Present Capacity: 251375177741 (234.11 GB)
DFS Remaining: 251355512832 (234.09 GB)
DFS Used: 19664909 (18.75 MB)
....
$ hadoop namenode -format

$ hdfs fsck / 

$ hdfs dfsadmin -setSpaceQuota n directory
$ hdfs dfsadmin -clrSpaceQuota directory
$ hdfs dfsadmin -setQuota n directory
$ hdfs dfsadmin -clrQuota directory
```

