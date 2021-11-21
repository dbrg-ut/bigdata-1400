### Iterate with "for"

```bash
$ cd  
$ mkdir section1-7
$ cd section1-7
$ touch a-file b-file

```



###### sample 1

```bash
$ seq 1 10
1
2
3
...
10
$ for i in $(seq 1 10)
> do
> echo "Row Number $i"
> done
Row Number 1
Row Number 2
Row Number 3
Row Number 4
Row Number 5
Row Number 6
Row Number 7
Row Number 8
Row Number 9
Row Number 10

```

###### sample 2 

```bash
$ for i in hello 1 * 2 goodbye 
>do
>  echo "Looping ... i is set to $i"
>done

Looping ... i is set to hello
Looping ... i is set to 1
Looping ... i is set to 2
Looping ... i is set to goodbye

$ for i in hello 1 * 2 goodbye 
>do
>  echo "Looping ... i is set to $i"
>done

Looping ... i is set to hello
Looping ... i is set to 1
Looping ... i is set to a-file
Looping ... i is set to b-file
Looping ... i is set to 2
Looping ... i is set to goodbye
```



**A Real Sample** : download a list of urls in urls.txt

```bash
$ cat > urls.txt <<\EOF
> www.google.com
> www.duckduckgo.com
> EOF


```



```bash
$ curl -o google.html www.google.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12706    0 12706    0     0  11509      0 --:--:--  0:00:01 --:--:-- 11519
$ echo "www.google.com" | cut -d . -f 2
```



```bash
$ for url in $(cat urls.txt)
> do
> filename=$(echo $url | cut -d . -f2)
> echo downloading $url into $filename".html"
> curl -o $(echo $filename".html") $url
> echo download completed!
> done

downloading www.google.com into google.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12646    0 12646    0     0   1557      0 --:--:--  0:00:08 --:--:--  2776
download completed!
downloading www.duckduckgo.com into duckduckgo.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   303    0   303    0     0     58      0 --:--:--  0:00:05 --:--:--    73
download completed!

```

###### Convert it to a shell script file 

```bash
$ nano downloader.sh
#!/bin/sh
for url in $(cat $1)
i=1
do
	filename=$(echo $url | cut -d . -f2)
	echo downloading $url into $filename".html"
	curl -o $(echo $filename".html") $url
	echo '#'$i download completed!
	i=$(expr $i + 1)
done


```

 ###### download the URLs

```bash
$ chmod -u=rwx downloader.sh
$ ./downloader.sh urls.txt
downloading www.google.com into google.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12694    0 12694    0     0   6041      0 --:--:--  0:00:02 --:--:--  6044
#1 download completed!
downloading www.duckduckgo.com into duckduckgo.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   303    0   303    0     0    275      0 --:--:--  0:00:01 --:--:--   275
#2 download completed!
```





### Conditionals with "if"



```bash
$ touch sourcefile 
 # Create two files; source is older than destination
$ touch destfile
```

```bash
$ if test sourcefile -nt destfile ; then
# Refresh if needed
   cp sourcefile destfile
   echo Refreshed destfile
fi
#nothing happens
```

```bash
$ touch sourcefile
 # Make source newer than destination
if [ sourcefile -nt destfile ] ; then
# Alternative test syntax
   cp sourcefile destfile
   echo Refreshed destfile
fi

Refreshed destfile
```

```bash
if [ sourcefile -nt destfile ] ; then
   cp sourcefile destfile
   echo Refreshed destfile
 else
   echo destfile is up to date
 fi

destfile is up to date
```



##### improve downloader.sh

```bash
#!/bin/sh
i=1
if [ $# -eq 1 ] ; then
        output=.
else
        if [ ! -d $2 ] ; then
                mkdir $2
        fi
        output=$2
fi

for url in $(cat $1)
do
        filename=$(echo $url | cut -d . -f2)
        echo downloading $url into $output/$filename".html"
        curl -o $(echo $output/$filename".html") $url
        echo '#'$i download completed!
        i=$(expr $i + 1)
done
```

```bash
$ ./downloader.sh  urls.txt downloads
downloading www.google.com into downloads/google.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12680    0 12680    0     0   7188      0 --:--:--  0:00:01 --:--:--  7192
#1 download completed!
downloading www.duckduckgo.com into downloads/duckduckgo.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   303    0   303    0     0    542      0 --:--:-- --:--:-- --:--:--   543
#2 download completed!

$ ls -lh downloads
total 16K
-rw-r--r-- 1 mojtaba mojtaba 303 Dec 24 12:09 duckduckgo.html
-rw-r--r-- 1 mojtaba mojtaba 13K Dec 24 12:09 google.html
```





### Loops with "while"

```bash
$ x=1
$ while [ $x -le 5 ]
> do
>  echo "Welcome $x times"
>  x=$(( $x + 1 ))
>  # x=$(expr $x + 1)
> done
Welcome 1 times
Welcome 2 times
Welcome 3 times
Welcome 4 times
Welcome 5 times
```



```bash
$ cat /etc/passwd |
> while read line; do
> echo $(echo $line | cut -d : -f 1 )
> done
root
daemon
bin
sys
sync
games
...
```



```bash
 $ cd /etc
 $ ls |
 # List all directory entries
> while read name ; do
 # For every entry
> if [ -f $name -a -r $name ] ; then
 # If regular file and readable
> echo -n "$name "
 # Display its name
> expr $(wc -c < $name) / $(wc -l < $name)
 # Display average characters per line
> fi
> done |
> head -n20
 # Display first ten lines
adduser.conf 34
bash.bashrc 32
bash_completion 45
bindresvport.blacklist 24
ca-certificates.conf 40
ca-certificates.conf.dpkg-old 41
crontab 47
crypttab 54
debconf.conf 35
debian_version 13
...
```



### Some Sample Pipeline With "xargs"


```bash
$ cd /etc
$ find . -type f |
 # Output the name of all files
> xargs cat |
 # Combine them by applying cat
> wc -l
 # Count number of lines

# to supress the errors
find . -type f 2>/dev/null | xargs cat 2>/dev/null | wc -l
```

###### Find The Oldest File in the Windows Program Files Folder 

```bash
$ find '/mnt/c/Program Files/' -type f 2>/dev/null  |
 # Output names under program files
> xargs stat -c '%Y %n' |
 # Output modification time (ts) and name
> sort -n |
 # Output in numeric order
> head -1
 # Output oldest one
 # a lot of Errors!
stat: cannot stat 'Files/ByteFence/Cache/SR1e2290d7436ea1a55c414cd42de46683f7d2e9bb': No such file or directory
stat: cannot stat '/mnt/c/Program': No such file or directory
stat: cannot stat 'Files/ByteFence/Cache/SR1e35b3b43380337d9ccb10a884de16ff39a5674f': No such file or directory
stat: cannot stat '/mnt/c/Program': No such file or directory
stat: cannot stat 'Files/ByteFence/Cache/SR1e3a3500991d526a0d514a68d28ce8cafdf047c6': No such file or directory
stat: cannot stat '/mnt/c/Program': No such file or directory 

ctrl+c 

```



 ###### Solution : custom file name separator

```bash
$ find '/mnt/c/Program Files/' -type f -print0 2>/dev/null  |
 # Output names under program files
> xargs -0 stat -c '%Y %n' 2>/dev/null |
 # Output modification time (ts) and name
> sort -n |
 # Output in numeric order
> head -1
 # Output oldest one
315520200 /mnt/c/Program Files/Typora/LICENSES.chromium.html
$  date --date=@315520200
Tue Jan  1 00:00:00 +0330 1980
```




### Select with "case"


```bash
$ uname
 # Operating system details
Linux $

$ case $(uname) in
 Linux)
   alias s="Linux OS"
   ;;
 Darwin)
   alias s="Apple Mc"
   ;;
esac
 
```

```bash
$ alias
...
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
alias s='Linux OS'
```


