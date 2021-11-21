### Archive listing

```bash
$ mkdir section2-1 && cd section2-1

```



```bash
$ curl -Ls https://mirrors.edge.kernel.org/pub/linux/kernel/v1.0/linux-1.0.tar.gz |
> tar -tzvf - |
> head -10
drwxr-xr-x root/root         0 1994-03-14 01:20 linux/
-rw-r--r-- root/root      6891 1994-03-14 02:08 linux/Makefile
drwxr-xr-x root/root         0 1994-03-13 22:09 linux/boot/
-rw-r--r-- root/root      9187 1993-12-01 16:14 linux/boot/bootsect.S
-rw-r--r-- root/root     17689 1993-12-01 16:14 linux/boot/setup.S
-rw-r--r-- root/root      8651 1994-02-03 14:07 linux/boot/head.S
drwxr-xr-x root/root         0 1994-03-13 22:09 linux/fs/
-rw-r--r-- root/root      4832 1993-12-01 16:14 linux/fs/stat.c
-rw-r--r-- root/root      1835 1993-12-21 14:00 linux/fs/Makefile
-rw-r--r-- root/root      2513 1993-12-01 16:14 linux/fs/read_write.c
```



### Extract files

```bash
$ curl -Ls  https://mirrors.edge.kernel.org/pub/linux/kernel/v1.0/linux-1.0.tar.gz |
> tar -xzvf -
linux/
linux/Makefile
linux/boot/
linux/boot/bootsect.S
linux/boot/setup.S
linux/boot/head.S
linux/fs/
linux/fs/stat.c
linux/fs/Makefile
linux/fs/read_write.c
linux/fs/block_dev.c
....
```



```bash
$ ls
linux
```

```bash
$ du -sh linux # Summarize/Human Readable
7.6M   linux
$ ls linux
CHANGES  CREDITS    Makefile  boot       drivers  ibcs     init  kernel  makever.sh  net  zBoot	COPYING  Configure  README    config.in  fs       include  ipc   lib   mm   tools
```



### Create an archive



```bash
 $ tar -cf dict.tar /usr/share/dict
 # Create archive from files
 tar: Removing leading `/' from member names 
```


```bash
$ tar -cf - /usr/share/dict |
 # Create archive to stdout
> gzip -c > dict.tar.gz  # Compress
tar: Removing leading `/' from member names
$ ls -lh
# See file size (in human-readable units)
-rw-r--r-- 1 mojtaba mojtaba 470K Dec 25 15:54 dict.tar
-rw-r--r-- 1 mojtaba mojtaba 128K Dec 25 16:53 dict.tar.gz

 $ du -sh /usr/share/dict
 # Obtain directory size
 460K    /usr/share/dict
```


##### Shorthand for gzip compression
```bash
 $ tar -czf dict2.tar.gz /usr/share/dict
 # Shorthand for gzip compression
 ls -lh
total 768K
-rw-r--r-- 1 mojtaba mojtaba 470K Dec 25 15:54 dict.tar
-rw-r--r-- 1 mojtaba mojtaba 128K Dec 25 16:53 dict.tar.gz
-rw-r--r-- 1 mojtaba mojtaba 128K Dec 25 16:56 dict2.tar.gz
drwxr-xr-x 1 mojtaba mojtaba  512 Mar 14  1994 linux
```



### Connect archive commands


```bash
$ ls /usr/share/dict
README.select-wordlist  american-english-small  words
$ mkdir dict2
```

###### Subshells

```bash
$ (
> cd /usr/share/dict
> tar -cf - .
> ) | (
> cd dict2
> tar -xf -
> )
$ ls -lh dict2
total 508K
-rw-r--r-- 1 mojtaba mojtaba  199 Nov 15  2018 README.select-wordlist
-rw-r--r-- 1 mojtaba mojtaba 458K Apr 25  2018 american-english-small
lrwxrwxrwx 1 mojtaba mojtaba   30 Dec 10 15:35 words -> /etc/dictionaries-common/words
```

###### Second Option

```bash
$ tar -C /usr/share/dict -cf - . | tar -C dict2 -xf -
```

####  List zip file contents

```bash
$ sudo apt install unzip
$ curl -o sample.zip https://file-examples-com.github.io/uploads/2017/02/zip_2MB.zip
$ unzip -v  sample.zip | head
Archive:  sample.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2017-10-31 01:06   zip_10MB/
   236789  2017-09-25 13:23   zip_10MB/file_example_ODS_5000.ods
  1028608  2017-08-11 00:45   zip_10MB/file_example_PPT_1MB.ppt
  1027072  2017-08-02 15:58   zip_10MB/file-sample_1MB.doc
---------                     -------
  2292469                     4 files

$ unzip  sample.zip
Archive:  sample.zip
   creating: zip_10MB/
  inflating: zip_10MB/file_example_ODS_5000.ods
  inflating: zip_10MB/file_example_PPT_1MB.ppt
  inflating: zip_10MB/file-sample_1MB.doc
```


#####  Compress data 

```bash
$ ls -lh dict.tar.gz
-rw-r--r-- 1 mojtaba mojtaba 128K Dec 25 16:53 dict.tar.gz 
$ gzip -dc < dict.tar.gz | bzip2 -c > dict.tar.bz2
$ ls -lh dict.tar.bz2
-rw-r--r-- 1 mojtaba mojtaba 160K Dec 25 17:47 dict.tar.bz2
```

