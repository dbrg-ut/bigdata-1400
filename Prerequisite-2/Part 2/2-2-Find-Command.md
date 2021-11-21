### Recurse directories with find

```bash
$ cd /usr
$ find . | head
# List all entries under the current directory
.
./bin
./bin/aa-enabled
./bin/aa-exec
./bin/add-apt-repository
./bin/addpart
./bin/apport-bug
./bin/apport-cli
./bin/apport-collect
./bin/apport-unpack
```

### Limit listing to files

```bash
$ find . -type f | head
# List only files
./bin/aa-enabled
./bin/aa-exec
./bin/add-apt-repository
./bin/addpart
./bin/apport-bug
./bin/apport-cli
./bin/apport-unpack
./bin/appres
./bin/apt
./bin/apt-cache 
```

### Limit listing to directories

```bash
$ find . -type d | head
# List only directories
.
./bin
./games
./include
./include/iproute2
./include/libdmmp
./include/openvpn
./include/X11
./include/xfs
./lib
```

#### Find files by name

```bash
 $ find . -name '*.?' | head
 # List entries ending in with one char
./bin/pdb3.8
./bin/perl5.30.0
./bin/pydoc3.8
./bin/pygettext3.8
./bin/python3.8
./include/gawkapi.h
./include/iproute2/bpf_elf.h
./include/libdmmp/libdmmp.h
./include/mpath_cmd.h
./include/mpath_persist.h 
```

### Combine Options

```bash
$ find . -name test
 # List entries named test
$ find . -name test -type f
 # List files named test
```

### Act on the results

```bash
$ find . -type f -ls | head
 # List details of each entry
 find . -type f -ls | head -1
1125899907247411     32 -rwxr-xr-x   1 root     root        31248 May 19  2020 ./bin/aa-enabled
```

### Execute a command for each file

```bash
$ find /usr/share/doc -type f -name changelog.gz | wc -l
56
$ find /usr/share/doc -type f -name changelog.gz | cat -n | tail -1
56  /usr/share/doc/x11-utils/changelog.gz
$ find /usr/share/doc -type f -name changelog.gz -exec gzip -dc '{}' \; |
> wc -l
7908
```


### Putting it all together

```bash
$  find /var/log/apt/ -type f -not -name '*.log.gz'
/var/log/apt/eipp.log.xz
/var/log/apt/history.log
/var/log/apt/term.log
```

```bash
$ find . -type f -size +10M
./bin/snap
./lib/snapd/snap-bootstrap
./lib/snapd/snap-repair
...

$ find /etc/dovecot/conf.d -name "*.conf" -mtime 5
#  filter all files under the /etc/dovecot/conf.d directory that ends 
# with .conf and has been modified in the last five days
$ find / -mmin -60
# modified last hour
$ find / -amin -60
# accessed last hour
```

```bash
$ find /home/mojtaba/ -type d -perm 755 -exec chmod 0744 '{}' \;
$ find / -user www-data -type f  -exec chown nginx '{}' \;
$ find /var/log/ -name ''*.temp' -delete
$ find . -type f -name "*.mp3" -exec rm -f '{}' \;
$ find /tmp -type d -empty
```

```bash
$ sudo find /var -not -name '*.log' -type f -o -name '*.???' -type f
# -o for or  
$ sudo find /var -not -name '*.log' -type f -a -name '*.???' -type f
# -a for and
```


```bash
$ info find
```

