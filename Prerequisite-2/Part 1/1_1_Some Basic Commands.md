#### Clear The Screan

```
$ clear
```



#### Print Current Working Directory

```bash
$ pwd
/home/mojtaba
```



#### Current Date

```bash
$ date
Fri 21 Feb 2020 01:04:36 PM EET 
```



#### Calendar 

```bash
$ cal
December 2020
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```



#### Current User

```bash
$ whoami
mojtaba
```



#### Exit Current Terminal

```bash
$ exit
```



#### Word Counter

```bash
$  wc /usr/share/dict/words
 51142  51142 468474 /usr/share/dict/words
```



#### Basic Calculator

```bash
$ bc
bc 1.07.1
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006, 2008, 2012-2017 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
4 * 5 ^2
100
ctrl+d
```



#### Uptime

```bash
$ uptime
20:11:41 up 17 min,  0 users,  load average: 0.52, 0.58, 0.59
```



#### Disk Free Space

```bash
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on
rootfs         183659516 152966304  30693212  84% /
none           183659516 152966304  30693212  84% /dev
none           183659516 152966304  30693212  84% /run
none           183659516 152966304  30693212  84% /run/lock
none           183659516 152966304  30693212  84% /run/shm
none           183659516 152966304  30693212  84% /run/user
tmpfs          183659516 152966304  30693212  84% /sys/fs/cgroup
C:\            183659516 152966304  30693212  84% /mnt/c
D:\            235519996 114112008 121407988  49% /mnt/d
E:\            235519996 142063752  93456244  61% /mnt/e
G:\            270198780 227379920  42818860  85% /mnt/g
J:\            234927100  92903072 142024028  40% /mnt/j
```



#### Memory Stats

```bash
$ free
              total        used        free      shared  buff/cache   available
Mem:       12446028     8447672     3769004       17720      229352     3864624
Swap:      22957436      265228    22692208
```



#### Disk Usage

```bash
$  du   /usr/bin/
100732  /usr/bin/
$  du  -h /usr/bin/
99M     /usr/bin/

```





#### System  Overview  (Resources )

```bash
$ top 
top - 20:18:01 up 23 min,  0 users,  load average: 0.52, 0.58, 0.59
Tasks:   6 total,   1 running,   5 sleeping,   0 stopped,   0 zombie
%Cpu(s):  7.8 us,  6.8 sy,  0.0 ni, 84.8 id,  0.0 wa,  0.7 hi,  0.0 si,  0.0 st
MiB Mem :  12154.3 total,   3649.0 free,   8281.3 used,    224.0 buff/cache
MiB Swap:  22419.4 total,  22160.4 free,    259.0 used.   3742.4 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    8936    296    256 S   0.0   0.0   0:00.06 init
   10 root      20   0    8936    196    156 S   0.0   0.0   0:00.00 init
   11 mojtaba   20   0   18072   3540   2084 S   0.0   0.0   0:00.08 bash
   24 root      20   0    8936    196    156 S   0.0   0.0   0:00.01 init
   25 mojtaba   20   0   18072   3628   3536 S   0.0   0.0   0:00.31 bash
  126 mojtaba   20   0   18920   2148   1528 R   0.0   0.0   0:00.03 top
```



- press `q` for exit



#### Command List Info

```bash
$ info top
TOP(1)                                              User Commands                                              TOP(1)

NAME
       top - display Linux processes

SYNOPSIS
       top -hv|-bcEHiOSs1 -d secs -n max -u|U user -p pid -o fld -w [cols]

       The traditional switches `-' and whitespace are optional.

DESCRIPTION
       The top program provides a dynamic real-time view of a running system.  It can display system summary informa‐
       tion as well as a list of processes or threads currently being managed by the Linux kernel.  The types of sys‐
       tem  summary  information  shown  and the types, order and size of information displayed for processes are all
       user configurable and that configuration can be made persistent across restarts.
.....

```

- *use Up/Down Page Down/Page Up , q for quit*



```bash
$ info

General Commands
* Screen: (screen).             Full-screen window manager.

GNU organization
* Maintaining Findutils: (find-maint).
                                Maintaining GNU findutils

GNU Utilities
* dirmngr-client: (gnupg).      X.509 CRL and OCSP client.
* dirmngr: (gnupg).             X.509 CRL and OCSP server.
* gpg-agent: (gnupg).           The secret key daemon.
* gpg2: (gnupg).                OpenPGP encryption and signing tool.
* gpgsm: (gnupg).               S/MIME encryption and signing tool.

Individual utilities
* arch: (coreutils)arch invocation.             Print machine hardware name.
* b2sum: (coreutils)b2sum invocation.           Print or check BLAKE2 digests.
* base32: (coreutils)base32 invocation.         Base32 encode/decode data.
* base64: (coreutils)base64 invocation.         Base64 encode/decode data.
* basename: (coreutils)basename invocation.     Strip directory and suffix.
```

- *You can see the list of all available commands .*



#### User Groups

```bash
$ groups
mojtaba adm dialout cdrom floppy sudo audio dip video plugdev netdev
$ groups mojtaba 
mojtaba : mojtaba adm dialout cdrom floppy sudo audio dip video plugdev netdev
```

- you can create a new group with : ***sudo groupadd newgroup***
  



#### ID Command

*This command prints user and groups (UID and GID) of the current user*

```bash
$ id
uid=1000(mojtaba) gid=1000(mojtaba) groups=1000(mojtaba),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev)
```



#### What IS This?

 *one line description about the given command*

```bash
$ whatis date
date (1)             - print or set the system date and time
```



#### Which Is This ?

 *locate a command*

```bash
$ which ls
/usr/bin/ls

$ which python

```



#### Change Password

```bash
$ passwd 
Changing password for mojtaba.
Current password:****
New password:****
Retype new password:****
```



####  user add, user delete command 

######  Commands With Super User Privilege

```bash
$ useradd test
useradd: Permission denied.
useradd: cannot lock /etc/passwd; try again later.
$ sudo useradd test
$ passwd test
passwd: You may not view or modify password information for test.
$ sudo passwd test
New password: ****
Retype new password:****
passwd: password updated successfully
$ sudo userdel test
```


#### 	SU :  Substitute User

```bash
$ su test
Password:
### change current user
$ whoami
test
$ exit
$ whoami
mojtaba
$ sudo su - test
### login as test
$ sudo -u test ls
### run ls as user test

```





#### Touch A File!

update access time of a file or create an empty file

```bash
$ touch a
$ touch b
```



#### List Files

```bash 
$ ls
a  b
$ ls -l
total 0
-rw-r--r-- 1 mojtaba mojtaba 0 Dec 17 23:09 a
-rw-r--r-- 1 mojtaba mojtaba 0 Dec 17 23:09 b
 
```




#### Apt/Yum/Snap ....

*package manages*

```bash
$ sudo apt update
$ sudo apt install python3
```



##### User Commands History

```bash
$ history
    1  ls
    2  pwd
    3  ls -1
    4  ls -l
    5  man ls
    6  mkdir temp
    7  cd temp/
    8  touch a
    9  touch b
   10  ls
```



#### Change File Permission/ File Owner 

```bash
$ cd
$ touch note.txt
$ sudo adduser editor
Adding user `editor' ...
Adding new group `editor' (1003) ...
Adding new user `editor' (1003) with group `editor' ...
Creating home directory `/home/editor' ...
Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for editor
Enter the new value, or press ENTER for the default
        Full Name []: Editor
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] Y
$ sudo usermod -a -G mojtaba editor
### Append editor to Group mojtaba
$ groups editor
editor : editor mojtaba
$ ls -l
total 0
-rw-r--r-- 1 mojtaba mojtaba 0 Dec 18 11:11 note.txt
$ su editor
Password : 
$ rm note.txt
rm: remove write-protected regular empty file 'note.txt'? yes
rm: cannot remove 'note.txt': Permission denied
$ exit
$ chmod u=rwx,g=rw,o=r /home/mojtaba
or 
$ chmod 764 /home/mojtaba
# give user the write permission so he could remove a file
$ su editor 

$ rm notes
$ exit
$ touch notes.txt
$ sudo chown editor:editor notes.txt
$ ls -l
total 0
-rw-r--r-- 1 editor editor 0 Dec 18 11:56 notes.txt
```



####  