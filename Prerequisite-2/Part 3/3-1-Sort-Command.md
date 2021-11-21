### Use grep to select date fields

```bash
$ cd 
$ mkdir section3-1 && cd section3-1
$ cat > dates <<\EOF
>Wed, 16 Jan 2008 11:19:57 +0200
>Sun, 18 Dec 2011 21:14:33 +0200
>Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
>Date : 
>Tue, 11 Sep 2007 21:46:55 -0700
>Sat, 11 Sep 2010 08:10:37 +0300
>Mon, 17 Dec 2007 21:05:46 +0200
>Sun, 25 Dec 2011 23:35:27 +0200
>Thu, 18 Dec 2003 12:02:55 -0500 (EST)
>date >
>Thu, 1 Apr 2004 10:25:14 +0300
>EOF

$ head dates -2
Wed, 16 Jan 2008 11:19:57 +0200
Sun, 18 Dec 2011 21:14:33 +0200

```

### Clean up the data

```bash
$ sort dates 
Date :
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Mon, 17 Dec 2007 21:05:46 +0200
Sat, 11 Sep 2010 08:10:37 +0300
Sun, 18 Dec 2011 21:14:33 +0200
Sun, 25 Dec 2011 23:35:27 +0200
Thu, 1 Apr 2004 10:25:14 +0300
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Tue, 11 Sep 2007 21:46:55 -0700
Wed, 16 Jan 2008 11:19:57 +0200
date
```



```bash
$ grep '[Dd]ate' dates 
Date :
date

$ grep -v '[Dd]ate' dates > dates.clean && mv dates.clean dates
# Cleanup the file
$ sort dates
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Mon, 17 Dec 2007 21:05:46 +0200
Sat, 11 Sep 2010 08:10:37 +0300
Sun, 18 Dec 2011 21:14:33 +0200
Sun, 25 Dec 2011 23:35:27 +0200
Thu, 1 Apr 2004 10:25:14 +0300
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Tue, 11 Sep 2007 21:46:55 -0700
Wed, 16 Jan 2008 11:19:57 +0200
...
```



### Sort by fields



```bash
$ sort -k 2 dates 
# Sort by second and subsequent fields
Thu, 1 Apr 2004 10:25:14 +0300
Tue, 11 Sep 2007 21:46:55 -0700
Sat, 11 Sep 2010 08:10:37 +0300
Wed, 16 Jan 2008 11:19:57 +0200
Mon, 17 Dec 2007 21:05:46 +0200
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Sun, 18 Dec 2011 21:14:33 +0200
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Sun, 25 Dec 2011 23:35:27 +0200 

$ sort -k 2,2 -k 1,1 dates | head -5
# Sort by second, then first field
Thu, 1 Apr 2004 10:25:14 +0300
Sat, 11 Sep 2010 08:10:37 +0300
Tue, 11 Sep 2007 21:46:55 -0700
Wed, 16 Jan 2008 11:19:57 +0200
Mon, 17 Dec 2007 21:05:46 +0200
Sun, 18 Dec 2011 21:14:33 +0200
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Sun, 25 Dec 2011 23:35:27 +0200 

$ sort -k 5.5,5.6 dates 
# Sort by time minutes
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Mon, 17 Dec 2007 21:05:46 +0200
Sat, 11 Sep 2010 08:10:37 +0300
Sun, 18 Dec 2011 21:14:33 +0200
Wed, 16 Jan 2008 11:19:57 +0200
Thu, 1 Apr 2004 10:25:14 +0300
Sun, 25 Dec 2011 23:35:27 +0200
Tue, 11 Sep 2007 21:46:55 -0700
Fri, 22 Oct 2004 06:58:32 -0400 (EDT) 
```


### Reverse sorting

```bash
$ sort -k 4 dates 
# Sort by year
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Thu, 1 Apr 2004 10:25:14 +0300
Mon, 17 Dec 2007 21:05:46 +0200
Tue, 11 Sep 2007 21:46:55 -0700
Wed, 16 Jan 2008 11:19:57 +0200
Sat, 11 Sep 2010 08:10:37 +0300
Sun, 18 Dec 2011 21:14:33 +0200
Sun, 25 Dec 2011 23:35:27 +0200

$ sort -k 4r dates 
# Reverse sort by year
Sun, 25 Dec 2011 23:35:27 +0200
Sun, 18 Dec 2011 21:14:33 +0200
Sat, 11 Sep 2010 08:10:37 +0300
Wed, 16 Jan 2008 11:19:57 +0200
Tue, 11 Sep 2007 21:46:55 -0700
Mon, 17 Dec 2007 21:05:46 +0200
Thu, 1 Apr 2004 10:25:14 +0300
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Thu, 18 Dec 2003 12:02:55 -0500 (EST) 

```

### Sort by month

```bash
 $ sort -k 3 dates 
 # Alphabetic sort by month
Thu, 1 Apr 2004 10:25:14 +0300
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Mon, 17 Dec 2007 21:05:46 +0200
Sun, 18 Dec 2011 21:14:33 +0200
Sun, 25 Dec 2011 23:35:27 +0200
Wed, 16 Jan 2008 11:19:57 +0200
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Tue, 11 Sep 2007 21:46:55 -0700
Sat, 11 Sep 2010 08:10:37 +0300 

$ sort -k 3M dates
# Chronological sort by month
Wed, 16 Jan 2008 11:19:57 +0200
Thu, 1 Apr 2004 10:25:14 +0300
Sat, 11 Sep 2010 08:10:37 +0300
Tue, 11 Sep 2007 21:46:55 -0700
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Mon, 17 Dec 2007 21:05:46 +0200
Sun, 18 Dec 2011 21:14:33 +0200
Sun, 25 Dec 2011 23:35:27 +0200
Thu, 18 Dec 2003 12:02:55 -0500 (EST)

$ sort -k 3M -k 2n dates
# .. and then by numerical day
Wed, 16 Jan 2008 11:19:57 +0200
Thu, 1 Apr 2004 10:25:14 +0300
Sat, 11 Sep 2010 08:10:37 +0300
Tue, 11 Sep 2007 21:46:55 -0700
Fri, 22 Oct 2004 06:58:32 -0400 (EDT)
Mon, 17 Dec 2007 21:05:46 +0200
Sun, 18 Dec 2011 21:14:33 +0200
Thu, 18 Dec 2003 12:02:55 -0500 (EST)
Sun, 25 Dec 2011 23:35:27 +0200

```

### Specify field delimiter

```bash
$ head -5 /etc/passwd
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
```

#### Sort by numeric group-id

```bash
$ sort -t : -k 4n /etc/passwd
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
```

### Merge sorted files

```bash
$ sort dates > sorted
$ sort -C dates && echo 'Sorted!'
# See if file is sorted (no)
$ sort -C sorted && echo 'Sorted!'
# See if file is sorted (yes)
Sorted!

$ time sort dates dates >/dev/null
 # Sort two files
```

### Sort suffixed numbers

```bash
 $ du -h  /usr/share/man |
 # Output disk usage in human-readable form
> sort -rh |
 # Order human-readable numbers (in reverse)
> head -10
16M     /usr/share/man
5.2M    /usr/share/man/man1
3.6M    /usr/share/man/man8
1.4M    /usr/share/man/man5
1.3M    /usr/share/man/man7
516K    /usr/share/man/fr
504K    /usr/share/man/de
368K    /usr/share/man/it
344K    /usr/share/man/ja
292K    /usr/share/man/ru
``` 