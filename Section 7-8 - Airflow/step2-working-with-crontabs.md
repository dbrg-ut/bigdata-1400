#### Step 1 : Get tweets every 5 minutes

```bash
$ mkdir -p /home/mojtaba/data/stage/
$ cd /home/mojtaba/data/stage/
$ mkdir step1 step2
$ cd /home/mojtaba/data
$ mkdir lake logs

$ crontab -l
no crontab for mojtaba

$ sudo usermod -a -G crontab $(whoami)
[sudo] password for mojtaba:
$ sudo service cron restart
$ crontab -e

    * * * * * /usr/bin/date > /home/mojtaba/test.txt

$ watch -n 5 ls -lh .


* * * * * /use/bin/curl -s -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | /usr/bin/jq '>  /home/mojtaba/data/stage/step1/$(date +%s).csv

Not WORKS !!!!!!!!!!!!!!!!

$ mkdir -p /home/mojtaba/data/scripts
$ cd /home/mojtaba/data/scripts
$ nano get_tweets.sh
#!/usr/bin/bash
/usr/bin/curl -s -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | /usr/bin/jq '.items[] | [.id, .sendTime, .sendTimePersian, .senderName, .senderUsername, .type, .content] | join(",") ' > /home/mojtaba/data/stage/step1/$(date +%s).csv

$ chmod +x  ./get_tweets.sh
$ crontab -e 

* * * * * /home/mojtaba/data/scripts/get_tweets.sh


$ cd /home/mojtaba 
$ watch -n 5 ls -lh data/stage


```



####  Step 2 : Combine CSV files every Hour 

```bash
$ cd /home/mojtaba/data/scripts
$ nano  combine_csv.sh
#! /usr/bin/bash

sleep 20;

flist=$(ls /home/mojtaba/data/stage/step1)
stage1="/home/airflow/data/stage/step1"
stage2="/home/airflow/data/stage/step2"
fname="$stage2/$(date +%Y-%m-%d-%H).csv"
logfile=/home/airflow/data/logs/step2.log

echo "Begin at $(date)" >> $logfile
for i in $flist ; do
        echo $i >> $logfile;
        current="$stage1/$i";
        echo "concatenating $current into $fname " >> $logfile ;
        sed -i "s/\"//g" $current;
        cat $current >> $fname;
        echo "deleting $current ..." >> $logfile;
        rm $current;
done;
echo "Sucessful" >> $logfile

$ chmod +x ./combine_csv.sh
$ crontab -e
...
59 * * * * /home/mojtaba/data/scripts/combine_csv.sh


$ tail -f /home/mojtaba/data/logs/step2.log
```



#### Step3 : Convert CSV files to Parquet every hour

```bash
$ sudo apt install python3 python3-pip virtualenv launchpadlib
$ pip3 install pandas pyarrow
$ cd /home/mojtaba/data/scripts
$ nano convert_to_parquet.py

#!/usr/bin/python3

import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], header=None , names=['id','sendTime','sendTimePersian', 'senderName', 'senderUsername', 'type', 'content' ],dtype={'content': object})
df.to_parquet( f"{sys.argv[2]}/{sys.argv[1].split('/')[-1].split('.')[0]}.parquet")

$ python3 convert_to_parquet.py /home/mojtaba/data/stage/step2/2021-02-13-20.csv /home/mojtaba/data/lake/

$ nano /home/mojtaba/data/scripts/convert_to_parquet.sh

!#/usr/bin/bash
stage2="/home/mojtaba/data/stage/step2"
flist=$(ls $stage2)
lake=/home/mojtaba/data/lake
logfile=/home/mojtaba/data/logs/step3.log

echo "Begin at $(date)" >> $logfile
for i in $flist ; do
        echo $i >> $logfile;
        current="$stage2/$i";
        echo "converting $current to parquet " >> $logfile ;
        /usr/bin/python3 /home/mojtaba/data/scripts/convert_to_parquet.py $current $lake ;        
        echo "deleting $current ..." >> $logfile;
done;
echo "Sucessful" >> $logfile

$ chmod +x ./convert_to_parquet.sh

$ crontab -e
10 * * * * /home/mojtaba/data/scripts/convert_to_parquet.sh
```





#### View  Parquet Contents



```bash
$ pip3 install parquet-cli
$ parq input.parquet --head 10
```

