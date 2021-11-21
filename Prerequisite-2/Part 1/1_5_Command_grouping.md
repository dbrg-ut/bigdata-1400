### Pipelines ,Boolean Operators & Command Grouping

*How Many Files Are There in /etc?*

**Step 0 : ** wc command

```bash
$ cd
$ mkdir  section1-5
$ cd section1-5
$ wc /usr/share/dict/words
51142  51142 468474 /usr/share/dict/words 
# Count lines, words, characters
```

**Step 1 :** store file list in a file

```bash
$ ls /etc >files
$ head files
NetworkManager
PackageKit
X11
adduser.conf
alternatives
apparmor
apparmor.d
apport
apt
at.deny
```
**Step 2: ** count lines of above file using wc

```bash
$ wc -l < files
185
$ wc -l files 
185 files
```



**All Steps in One Command : Make a Pipeline **

```bash
$ ls /etc | wc -l 
185 
```

**another way :** 

```bash
 $ ls /etc | cat -n
 $ ls /etc | cat -n | tail -1
```



### Exit code


```bash
$ wc files
# Run a command that succeeds
185  185 1806 files
$ echo $?
# Print exit status (zero)
0 $
$ wc xyz
# Run a command that fails
wc: xyz: No such file or directory
echo $?
 # Print exit status (non-zero)
1 

```


**if One step in pipeline fails, the remaining tasks would fail, too **

```bash
$ ls /ec | cat -n | tail -1
ls: cannot access '/ec': No such file or directory
```

### The and operator &&

```bash
$ rm files
$ touch a-file
$ cat -n a-file > b-file && rm a-file
 # Execute second only if first succeeds
$ ls
b-file 
$ cat -n bfile >cfile && rm b-file
 # Note typo; command will fail
cat: bfile: No such file or directory 
$ ls
b-file  cfile 
```



### The or operator ||


```bash
$ touch a-file
$ cp a-file b-file || echo Copy failed
 # Command that succeeds
$ cp afile bfile || echo Copy failed
 # Note typo
cp: cannot stat 'afile': No such file or directory 
Copy failed 
```



### The negation operator !

```bash
 $ ! date
# Command that succeeds
Fri 21 Feb 2020 01:11:49 PM EET $  
$ echo $?
1 
$ ! ls xyzzy
# Command that fails
ls: cannot access xyzzy: No such file or directory 
$ echo $?
0 
$ ! date &&  echo Hi
Wed Dec 23 23:12:18 +0330 2020
$ ! date || echo Hi
Wed Dec 23 23:14:56 +0330 2020
Hi
```


### Command grouping

```bash
$ echo -n 'Today is: ' ; date
# Execute two commands in a row
Today is: Fri 21 Feb 2020 01:05:31 PM EET 

$ { echo -n 'Today is: ' ; date ; } >timestamp
 # Redirect output of both
$ cat timestamp
Today is: Fri 21 Feb 2020 01:05:35 PM EET 
$ { echo -n 'Today is: ' ; date ; } | wc -c
 # Pipe output of both
39 
$ {
 # Group on multiple lines
   echo -n 'Today is: '
   date
 }
Today is: Fri 21 Feb 2020 01:05:42 PM EET 
```



#### xargs

The `xargs` command in UNIX is a command line utility for building an execution pipeline from standard input. Whilst tools like [`grep`](https://shapeshed.com/unix-grep/) can accept standard input as a parameter, many other tools cannot



```bash
$ echo a-dir | mkdir
mkdir: missing operand
Try 'mkdir --help' for more information.

$ date | echo 

# empty output

```



*some commands **does not accept parameters from standard input**.*

try using ***xargs***

```bash
$ echo 'one two three' | xargs mkdir
$ ls 
a-file  b-file  cfile  one  three  two

$ date | xargs echo
Wed Dec 23 23:21:40 +0330 2020

$ ! date | xargs echo
Wed Dec 23 23:22:53 +0330 2020

$  find  *file | xargs rm

$ echo 'd1 d2 d3' | xargs -t mkdir
mkdir d1 d2 d3
$ rm -r d* 

$ echo 'd1 d2 d3' | xargs -t -n 1 mkdir
mkdir d1
mkdir d2
mkdir d3
$ rm -r d* 

$ echo 'd1 d2 d3' | xargs -t -n 2 mkdir
mkdir d1 d2
mkdir d3
$ rm -r d* 
```

