### Exploring a Git Repository : Days by number of commits

#### A Practical Sample

```bash
$ sudo apt install git
$ git clone https://github.com/getpelican/pelican
Cloning into 'pelican'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 20923 (delta 1), reused 4 (delta 1), pack-reused 20914
Receiving objects: 100% (20923/20923), 6.17 MiB | 624.00 KiB/s, done.
Resolving deltas: 100% (13926/13926), done.

$ cd pelican
```


```bash
$ git log --pretty=format:%aD |
 # Fetch commit dates
> cut -d, -f1 |
> sort |
 # Bring all weekdays together
> uniq -c |
 # Count weekday occurrences
> sort -rn
 # Order by descending popularity

525 Tue
523 Sun
500 Mon
496 Wed
484 Fri
474 Sat
411 Thu
```



### 1. Fetching



```bash
$ git log --pretty=format:%aD |
 # Fetch commit dates
> head
# Show first 10 lines
Tue, 1 Dec 2020 20:36:51 +0000
Tue, 1 Dec 2020 18:07:51 +0000
Sun, 22 Nov 2020 16:16:28 +0000
Sun, 22 Nov 2020 16:13:51 +0000
Fri, 20 Nov 2020 16:30:18 +0100
Fri, 20 Nov 2020 16:22:39 +0100
Fri, 20 Nov 2020 15:46:05 +0100
Fri, 20 Nov 2020 15:39:52 +0100
Mon, 2 Nov 2020 17:18:38 +0100
Mon, 2 Nov 2020 13:15:26 +0000
```


### 2. Selection



```bash
$ git log --pretty=format:%aD |
 # Fetch author commit dates
cut -d, -f1 |
 # Select the weekday
head
 # Short first 10
Tue
Tue
Sun
Sun
Fri
Fri
Fri
Fri
Mon
Mon 
```



### 3. Processing



```bash
$ git log --pretty=format:%aD |
 # Fetch commit dates
cut -d, -f1 |
 # Select the weekday
sort |
 # Bring all weekdays together
head
 # Show first 10 lines
Fri
Fri
Fri
Fri
Fri
Fri
Fri
Fri
Fri
Fri
```



### 4. Summarizing



```bash
 $ git log --pretty=format:%aD |
 # Fetch commit dates
cut -d, -f1 |
 # Select the weekday
sort |
 # Bring all weekdays together
uniq -c
 # Count weekday occurrences
484 Fri
500 Mon
474 Sat
523 Sun
411 Thu
525 Tue
496 Wed 
```



### 5. Reporting



```bash
$ git log --pretty=format:%aD |
 # Fetch commit dates
 cut -d, -f1 |
 # Select the weekday
 sort |
 # Bring all weekdays together
 uniq -c |
 # Count weekday occurrences
 sort -rn
 # Order by descending popularity
 
525 Tue
523 Sun
500 Mon
496 Wed
484 Fri
474 Sat
411 Thu
```

