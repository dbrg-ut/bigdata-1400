### Working with Files/Folders

```bash
$ cd  
$ mkdir test
$ cd test
$ pwd
 # Print working directory
/home/mojtab
```



#### CD command in more Detail


```bash
$ cd ..
 # Move up one directory level
$  pwd
/home/mojtaba 
$ cd ../..
 # Move up another directory level
 $ pwd
 /
 $ cd 
 # Go to your home directory
 $ pwd
 /home/mojtaba
 $ cd -
 # back to previous location
 $ pwd 
 /
```


#### Absolute Path

We can move into any folder specifying his absolute path
```bash
 $ cd /home/mojtaba/test
 $ cd /tmp
  # Move to the tmp directory under the root
```


```bash
$ cd /
$ ls
bin   dev  home  lost+found  mnt  proc  run   selinux  sys  usr  vol boot  etc  lib   media       opt  root  sbin  srv      tmp  var 
```

#### Relative path

```bash
 $ cd usr
 $ ls 
 bin  games  include  lib  local  sbin  share  src 

```



### File manipulation commands

```bash
$ cd ~/test
$ echo ali kamali >akamali

$ echo sara davari >sdavari
$ touch a-file
$ ls
a-file  akamali sdavari

```
####  Remove a file
```bash
 $ rm a-file
 $ ls
 aKamali sDavari
```


#### Change file's name
```bash
$ mv aKamali aKamali
$ mv sdavari sDavari
$ ls
aKamali sDavari
```


```bash
$ mkdir names
 # Create a directory
$  mv sDavari names/
# move without renaming
$  mv aKamali names/aliKamali.info
# move and rename 
$ ls -lh names/
total 0
-rw-r--r-- 1 mojtaba mojtaba 11 Dec 23 11:51 aliKamali.info
-rw-r--r-- 1 mojtaba mojtaba 12 Dec 23 11:52 sDavari
```

#### Copy file to current directory

```bash
$ cp names/aliKamali.info .
$ cp names/sDavari .
$ ls
aliKamali.info  names  sDavari
$ mv sDavari sDavari.info
$ cp *.info /home/mojtaba/
$ ls -lh /home/mojtaba/
total 0
drwxr-xr-x 1 mojtaba mojtaba 512 Dec 23 11:33 a
-rw-r--r-- 1 mojtaba mojtaba  11 Dec 23 12:38 aliKamali.info
-rw-r--r-- 1 mojtaba mojtaba   0 Dec 23 10:01 error
-rw-r--r-- 1 mojtaba mojtaba 179 Dec 22 23:39 if
-rw-r--r-- 1 mojtaba mojtaba  86 Dec 22 23:36 if-1
-rw-r--r-- 1 mojtaba mojtaba  93 Dec 22 23:37 if-2
lrwxrwxrwx 1 mojtaba mojtaba   2 Dec 23 11:04 if-complete -> if
-rw-r--r-- 1 mojtaba mojtaba 317 Dec 23 10:01 output
-rw-r--r-- 1 mojtaba mojtaba  12 Dec 23 12:38 sDavari.info
drwxr-xr-x 1 mojtaba mojtaba 512 Dec 23 12:38 test
```

#### Remove a Directory

```bash
$ cd ~
$ mkdir a-dir
$ rmdir a-dir
 # Remove directory
$ rmdir test/
rmdir: failed to remove 'test/': Directory not empty 
$ rm -r test/
$ mkdir test && cp *.info test/ && mkdir test/a-dir
$ rm test/*
rm: cannot remove 'test/a-dir': Is a directory
$ ls -lh test/
total 0
drwxr-xr-x 1 mojtaba mojtaba 512 Dec 23 12:46 a-dir
```

$

### Recursive directory hierarchies

```bash
$ mkdir files
$ touch files/a files/b
$ cp files files2
# Normal cp fails (message can vary)
cp: -r not specified; omitting directory 'files'
```

##### Copy a directory with the recursive flag
```bash
$ cp -r files files2
$ ls files2
a  b
$ ls -R
 # Recursive list of current directory
ls -R
.:
error  files  if  if-1  if-2  if-complete  if-hardlink  output

./files:
a  b

rm -rf files2
 # Remove specified directory with recursive and force flags
```

#### Editing a file in vim/nano

```bash 
$ nano if
```
Below are listed the options that you will see when you first open nano:

    G Get Help
    ^O Write Out
    ^W Where Is
    ^K Cut Text
    ^J Justify
    ^C Cur Pos
    M-U Undo
    ^X Exit
    ^R Read File
    ^\ Replace
    ^U Uncut Text
    ^T To Spell
    ^_ Go To Line
    M-E Redo
    
- M is used for Alt Key
- ^g for see the whole list of commands  (^x to exit)
- ^ for setting/unsetting Mark
- ^s or ^o: save changes
