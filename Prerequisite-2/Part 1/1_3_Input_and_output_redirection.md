### Output redirection



```bash
$ echo If you can keep your head when all about you >if-1
 # Output redirection
```



```bash
$ cat if-1
```

> If you can keep your head when all about you 



```bash
 echo Are losing theirs and blaming it on you, >>if-1
 # Append to file
```



```bash
 $ cat if-1
```

> If you can keep your head when all about you Are losing theirs and blaming it on you, 



```bash
 $ echo If you can trust yourself when all men doubt you, >if-2
```



```bash
 $ echo But make allowance for their doubting too. >>if-2
```



```bash
 $ cat if-2
```

> If you can trust yourself when all men doubt you, But make allowance for their doubting too. $

```bash
 $ cat if-1 if-2
 # Combine two files
```

> If you can keep your head when all about you Are losing theirs and blaming it on you, If you can trust yourself when all men doubt you, But make allowance for their doubting too. 



```bash
 $ cat if-1 if-2 >if
 # Output redirection
```



```bash
$ cat if
```

> If you can keep your head when all about you Are losing theirs and blaming it on you, If you can trust yourself when all men doubt you, But make allowance for their doubting too. 

- **Hint** : output files are created before executing the command

  ```bash
  $ ls > ls.txt
  $ cat ls.txt 
  ```

  

### The standard error channel


```bash
 touch afile
```



```bash
$ ls xyz >output
 # Display an error message
ls: cannot access xyzzy: No such file or directory 
```




```bash
$ cat output
 # output is created but empty
```



```bash
 $ ls xyz 2>output
 # Redirect error
```



```bash
$ cat output
ls: cannot access xyz: No such file or directory $

```

```bash
 $ ls -l afile xyz >output 2>error
 # Redirect output and error
```


```bash
 $ cat output
 -rw-r--r-- 1 dds dds 0 Dec  7 10:51 afile 

```


```bash
 $ cat error
 ls: cannot access xyzzy: No such file or directory $

```



### Input redirection



```bash
$ bc
40 + 2
42
scale = 60
sqrt(2)
1.414213562373095048801688724209698078569671875376948073176679 

```



```bash
$ echo 2 ^ 64 - 1 >chess-rice
$  bc <chess-rice
18446744073709551615

```


```bash
$ cat -n < if
```

​     1  If you can keep your head when all about you   

​     2  Are losing theirs and blaming it on you,    

​     3  If you can trust yourself when all men doubt you,     

​     4  But make allowance for their doubting too.



####  View File Content / Paging 

##### check file type before viewing it.

```bash
$ file /usr/share/dict/words
/usr/share/dict/words: symbolic link to /etc/dictionaries-common/words
$ ls -lh  /etc/dictionaries-common/words
lrwxrwxrwx 1 root root 38 Dec 10 15:35 /etc/dictionaries-common/words -> /usr/share/dict/american-english-small
$ file /etc/dictionaries-common/words
/etc/dictionaries-common/words: symbolic link to /usr/share/dict/american-english-small
$ file /usr/share/dict/american-english-small
/usr/share/dict/american-english-small: UTF-8 Unicode text

```



we can get more information about a file using ***stat*** command.

```bash
 $ stat  /usr/share/dict/words
 File: /usr/share/dict/words -> /etc/dictionaries-common/words
  Size: 30              Blocks: 0          IO Block: 512    symbolic link
Device: 2h/2d   Inode: 3096224744126870  Links: 1
Access: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2020-12-10 15:35:24.352755100 +0330
Modify: 2020-12-10 15:35:24.352755100 +0330
Change: 2020-12-10 15:35:24.352755100 +0330
 Birth: -
```



#### Symbolic Links (Soft Link) : a pointer to original file

```bash
$ readlink -f /usr/share/dict/words
/usr/share/dict/american-english-small
$ ln -s if if-complete
$ ls -lh
total 0
-rw-r--r-- 1 mojtaba mojtaba   0 Dec 23 10:01 error
-rw-r--r-- 1 mojtaba mojtaba 179 Dec 22 23:39 if
-rw-r--r-- 1 mojtaba mojtaba  86 Dec 22 23:36 if-1
-rw-r--r-- 1 mojtaba mojtaba  93 Dec 22 23:37 if-2
lrwxrwxrwx 1 mojtaba mojtaba   2 Dec 23 11:04 if-complete -> if
-rw-r--r-- 1 mojtaba mojtaba 317 Dec 23 10:01 output

$  cat if-complete
If you can keep your head when all about you
Are losing theirs and blaming it on you,
If you can trust yourself when all men doubt you,
But make allowance for their doubting too.

$ ln if if-hardlink
$ ls -lh
total 0
-rw-r--r-- 1 mojtaba mojtaba   0 Dec 23 10:01 error
-rw-r--r-- 2 mojtaba mojtaba 179 Dec 23 14:03 if
-rw-r--r-- 1 mojtaba mojtaba  86 Dec 22 23:36 if-1
-rw-r--r-- 1 mojtaba mojtaba  93 Dec 22 23:37 if-2
lrwxrwxrwx 1 mojtaba mojtaba   2 Dec 23 11:04 if-complete -> if
-rw-r--r-- 2 mojtaba mojtaba 179 Dec 23 14:03 if-hardlink
-rw-r--r-- 1 mojtaba mojtaba 317 Dec 23 10:01 output
# Consider Number2 in row 2, indicating if has 2 hard link : 1 to itself and the second for if-hardlink
$ rm if
$ ls -lh
# if-complete -> if shown in Red on Black, indicating broken link
-rw-r--r-- 1 mojtaba mojtaba   0 Dec 23 10:01 error
-rw-r--r-- 1 mojtaba mojtaba  86 Dec 22 23:36 if-1
-rw-r--r-- 1 mojtaba mojtaba  93 Dec 22 23:37 if-2
lrwxrwxrwx 1 mojtaba mojtaba   2 Dec 23 11:04 if-complete -> if
-rw-r--r-- 1 mojtaba mojtaba 179 Dec 23 14:03 if-hardlink
-rw-r--r-- 1 mojtaba mojtaba 317 Dec 23 10:01 output
$ cat if-complete
cat: if-complete: No such file or directory
$ cat if-hardlink
If you can keep your head when all about you
Are losing theirs and blaming it on you,
If you can trust yourself when all men doubt you,
But make allowance for their doubting too.
$ stat if-hardlink
  File: if-hardlink
  Size: 179             Blocks: 0          IO Block: 512    regular file
Device: 2h/2d   Inode: 13510798882340976  Links: 2
Access: (0644/-rw-r--r--)  Uid: ( 1000/ mojtaba)   Gid: ( 1000/ mojtaba)
Access: 2020-12-23 14:12:13.617244600 +0330
Modify: 2020-12-23 14:12:13.617244600 +0330
Change: 2020-12-23 14:12:33.943981900 +0330
 Birth: -
```

**A symbolic or soft link** is an actual **link** to the original file, whereas a **hard link** is a mirror copy of the original file

###### View File Contents

```bash
$ cat /usr/share/dict/words
 # So Many Lines / not so useful
$ head /usr/share/dict/words 
$ head -20 /usr/share/dict/words
$ tail /usr/share/dict/words
$ tail -20 /usr/share/dict/words
```


#### View File Content Page by Page

```bash
 $ more /usr/share/dict/words

African
African's
Africans
Allah
Allah's
American
American's
Americanism
Americanism's

```
- use f/b for scrolling up/down

```bash
 $  less  /usr/share/dict/words
African
African's
Africans
Allah
Allah's
American
American's
Americanism
Americanism's
```
- use f/b for scrolling up/down , Page Down/Up , Up/Down
- Less is more!
