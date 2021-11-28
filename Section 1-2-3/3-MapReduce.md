**Go to name node and install Python**

```bash
$ apt install python
$ apt install python-pip
$ pip install mrjob

$ python /data/wordcount.py /data/war-and-peace-tolstoy.txt
No configs found; falling back on auto-configuration
No configs specified for inline runner
Creating temp directory /tmp/wordcount.root.20210102.075125.806977
Running step 1 of 1...
job output is in /tmp/wordcount.root.20210102.075125.806977/output
Streaming final output from /tmp/wordcount.root.20210102.075125.806977/output...
"chars" 3221116
"words" 565427
"lines" 65222
Removing temp directory /tmp/wordcount.root.20210102.075125.806977...
```





##### Running Tasks with Hadoop

```bash
$ python /data/wordcount.py -r hadoop hdfs:///books/war-and-peace-tolstoy.txt

No configs found; falling back on auto-configuration
No configs specified for hadoop runner
Looking for hadoop binary in /opt/hadoop-3.2.1/bin...
Found hadoop binary: /opt/hadoop-3.2.1/bin/hadoop
Using Hadoop version 3.2.1
Looking for Hadoop streaming jar in /opt/hadoop-3.2.1...
Found Hadoop streaming jar: /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar
Creating temp directory /tmp/wordcount.root.20210102.075639.273084
uploading working dir files to hdfs:///user/root/tmp/mrjob/wordcount.root.20210102.075639.273084/files/wd...
Copying other local files to hdfs:///user/root/tmp/mrjob/wordcount.root.20210102.075639.273084/files/
Running step 1 of 1...


```

##### Error !!!

python must be installed in every `NodeManager`!