 ### Put Data in HDFS

```bash
 #### Go To Name Node
$ cd /data
$ hadoop fs -mkdir -p /data/imdb/title_basics
$ hadoop fs -mkdir -p /data/imdb/title_ratings
$ gunzip -k title.ratings.tsv.gz
$ gunzip -k title.basics.tsv.gz
$ hadoop fs -put title.basics.tsv  /data/imdb/title_basics/
$ hadoop fs -put title.ratings.tsv /data/imdb/title_ratings/
or 
$ gunzip -c title.basics.tsv.gz | hadoop fs -put - /data/imdb/title_basics/title.basics.tsv
$ gunzip -c title.ratings.tsv.gz | hadoop fs -put - /data/imdb/title_ratings/title.ratings.tsv
```



#### Create Database & Tables using DBeaver

```sql
CREATE DATABASE IF NOT EXISTS imdb;

USE imdb;

CREATE EXTERNAL TABLE IF NOT EXISTS title_ratings(
	tconst STRING,
	average_rating DECIMAL(2,1),
	num_votes BIGINT
) 
COMMENT 'IMDb Ratings'
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' 
STORED AS TEXTFILE 
LOCATION '/data/imdb/title_ratings'
TBLPROPERTIES ('skip.header.line.count'='1');


CREATE EXTERNAL TABLE IF NOT EXISTS title_basics (
	tconst STRING,
	title_type STRING,
	primary_title STRING,
	original_title STRING,
	is_adult DECIMAL(1,0),
	start_year DECIMAL(4,0),
	end_year STRING,
	runtime_minutes INT,
	genres STRING
) 
COMMENT 'IMDb Movies' 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE LOCATION '/data/imdb/title_basics'
TBLPROPERTIES ('skip.header.line.count'='1');

select * from title_basics limit 3;

select * from title_ratings  limit 10 ; 

select avg(average_rating) from title_ratings  limit 10 ; 

select * 
from title_ratings 
order by average_rating desc
limit 3;


SELECT * 
FROM title_basics b JOIN title_ratings r ON (b.tconst=r.tconst)
WHERE original_title = 'The Dark Knight' AND title_type='movie';

 
```



####  Getting Around

- Check Resource Manager
- Checkout HiveServer2 Web UI 
  - go to : http://localhost:10002
  - only for viewing `metadata` and `logs`	
- Check Postgres Meta Store
- Check and Work with hue 
  - ***uncomment*** the hue section ( 2 services ) in docker compose 
  - restart the cluster
  - visit http://localhost:8888

#### Beeline

Go to hive server container :
```bash
$ !connect jdbc:hive2://localhost:10000/default
user : hive
pass : hive


$ USE imdb;

$ !tables;
$ !quit

SHOW DATABASES;
USE <database>;

SHOW TABLES;
DESC <table>;
DESC FORMATTED <table>;
```

#### Move Data File 

go to NameNode and do the followings:

```bash
$ hadoop fs -ls -R /data
drwxr-xr-x   - root supergroup          0 2021-01-10 11:34 /data/imdb
drwxr-xr-x   - root supergroup          0 2021-01-10 12:37 /data/imdb/title_basics
-rw-r--r--   1 root supergroup  639907418 2021-01-10 12:37 /data/imdb/title_basics/title.basics.tsv
drwxr-xr-x   - root supergroup          0 2021-01-10 12:37 /data/imdb/title_ratings
-rw-r--r--   1 root supergroup   18954355 2021-01-10 12:37 /data/imdb/title_ratings/title.ratings.tsv

$ hadoop fs -mv /data/imdb/title_basics/title.basics.tsv /data/imdb/

#### Run : select * from title_basics limit 3;
 Done. 0 results.
$ hadoop fs -mv /data/imdb/title.basics.tsv /data/imdb/title_basics/title.basics.tsv

#### Run : select count(*)  from title_basics;
7498564

$ hadoop fs -cat  /data/imdb/title_basics/title.basics.tsv | wc -l
2021-01-10 13:10:41,331 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
7498565

 $ split -l 1000000 -d title.basics.tsv title.basics.
 header=$(head -1  title.basics.00)
 for i in  title.basics.0[1-7] ; do 
 > echo $i
 > sed -i "1i$header" $i
 > done
 
 
 $ hadoop fs -put title.basics.0[0-3] /data/imdb/title_basics
 $ hadoop fs -ls -R /data/imdb/title_basics
-rw-r--r--   1 root supergroup   /data/imdb/title_basics/title.basics.00
-rw-r--r--   1 root supergroup   /data/imdb/title_basics/title.basics.01
-rw-r--r--   1 root supergroup   /data/imdb/title_basics/title.basics.02
-rw-r--r--   1 root supergroup   /data/imdb/title_basics/title.basics.03

$ #### Run : select count(*)  from title_basics;
3999996
```



#### Some Advanced Queries

```sql

SELECT original_title, average_rating
FROM title_basics b JOIN title_ratings r ON (b.tconst=r.tconst)
WHERE original_title like '%love%' AND title_type='movie'
order by average_rating desc
limit 10 
;


SELECT primary_title , start_year , r.average_rating , genres , r.num_votes 
FROM title_basics b JOIN title_ratings r ON (b.tconst=r.tconst)
WHERE primary_title like '%love%' AND title_type='movie'
order by average_rating desc
limit 20
;

select b.primary_title, avg(r.average_rating) as rating
from title_basics b JOIN title_ratings r ON (b.tconst=r.tconst)
where title_type='movie' and start_year < 2021
group by primary_title
ORDER BY rating desc
limit 10;
```

#### Partitioning 

###### Static Partitioning

```sql
CREATE TABLE IF NOT EXISTS imdb_ratings_partitioned(
	tconst STRING,
	average_rating DECIMAL(2,1),
	num_votes BIGINT
) 
PARTITIONED BY (partition_quality STRING)
STORED AS ORCFILE LOCATION '/data/imdb/ratings_partitioned';



INSERT OVERWRITE TABLE imdb_ratings_partitioned partition(partition_quality='good')
SELECT r.tconst, r.average_rating, r.num_votes FROM title_ratings r WHERE r.average_rating >= 7;

INSERT OVERWRITE TABLE imdb_ratings_partitioned partition(partition_quality='worse')
SELECT r.tconst, r.average_rating, r.num_votes FROM title_ratings r WHERE r.average_rating < 7;


select distinct average_rating 
from imdb_ratings_partitioned 
where partition_quality = 'good'
order by average_rating desc;

```



###### Dynamic Partitioning

```sql
CREATE TABLE IF NOT EXISTS imdb_movies_partitioned(
	tconst STRING,
	title_type STRING,
	primary_title STRING,
	original_title STRING,
	is_adult DECIMAL(1,0),
	start_year DECIMAL(4,0),
	end_year STRING,
	runtime_minutes INT,
	genres STRING
) PARTITIONED BY (partition_year int)
STORED AS ORCFILE
LOCATION '/data/imdb/movies_partitioned';

set hive.exec.dynamic.partition.mode=nonstrict; 
-- enable dynamic partitioning
set hive.exec.max.dynamic.partitions=200;
set hive.exec.max.dynamic.partitions.pernode=200;


INSERT OVERWRITE TABLE imdb_movies_partitioned partition(partition_year)
SELECT m.tconst, m.title_type, m.primary_title, m.original_title, m.is_adult,
m.start_year, m.end_year, m.runtime_minutes, m.genres,
m.start_year -- last column = partition column
FROM title_basics m





```



###### Bucketing

```sql
set hive.enforce.bucketing = true

CREATE TABLE IF NOT EXISTS imdb_movies_partitioned_bucket(
	tconst STRING,
	title_type STRING,
	primary_title STRING,
	original_title STRING,
	is_adult DECIMAL(1,0),
	start_year DECIMAL(4,0),
	end_year STRING,
	runtime_minutes INT,
	genres STRING
) 
PARTITIONED BY (partition_year int)
 CLUSTERED BY (title_type) 
 SORTED BY (start_year) INTO 5 BUCKETS
STORED AS ORCFILE
LOCATION '/data/imdb/movies_partitioned_bucket';

set hive.exec.dynamic.partition.mode=nonstrict; 
-- enable dynamic partitioning
set hive.exec.max.dynamic.partitions=200;
set hive.exec.max.dynamic.partitions.pernode=200;
set hive.enforce.bucketing = true;

INSERT OVERWRITE TABLE imdb_movies_partitioned_bucket partition(partition_year)
SELECT m.tconst, m.title_type, m.primary_title, m.original_title, m.is_adult,
m.start_year, m.end_year, m.runtime_minutes, m.genres,
m.start_year -- last column = partition column
FROM title_basics m


```

