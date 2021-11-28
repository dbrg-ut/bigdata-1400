#### Hadoop Setup

> Make Sure Docker Desktop is Running!

Go to Command Line (in Windows, Open PowerShell) and run this to pull and start the Cluster :
```bash
$ cd docker
$ docker-compose up
```
#### Hadoop Configuration

refer to this address :

[Big Data Europe - Docker Hadoop](https://hub.docker.com/r/bde2020/hadoop-base/)

each hadoop setting can be customized : [hdfs-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)

##### Ports

- Namenode: http://localhost:9870
- History server: http://localhost:8188
- Datanode: http://localhost:9864
- Nodemanager: http://localhost:8042
- Resource manager: http://localhost:8088

