### egrep
##### Number of repetitions

```bash
$ egrep 'a{2}' /usr/share/dict/words
# /usr/share/dict/words with two a characters
aardvark
bazaar
bazaar's
bazaars

$ egrep "[^aeiouy\']{5}" /usr/share/dict/words
# /usr/share/dict/words with 5 consonants not including apastrof
birthplace
birthplace's
birthplaces
corkscrew
corkscrew's
corkscrewed
corkscrewing
corkscrews
downstream
...

$ egrep '^.{,3}$' /usr/share/dict/words | tail
# /usr/share/dict/words with a length up to 3
yak
yam
yap
yen
yes
yet
yew
you
zip
zoo

```



```bash
$ egrep '^.{15,}$' /usr/share/dict/words | wc -l
# /usr/share/dict/words with a length of at least 15
404
$ egrep '^.{14}.+$' /usr/share/dict/words | wc -l
404

$ egrep '^.{15,16}$' /usr/share/dict/words | wc -l
 # /usr/share/dict/words with a length between 15 and 16
362
$ egrep '^.{15}.?$' /usr/share/dict/words | wc -l
# Same using ? (one or zero)
362
```


### Back-references



```bash
$ egrep '^(.).*\1$' /usr/share/dict/words | head -3
# /usr/share/dict/words beginning and ending with same letter
# The \1 refers to the first captured group.
agenda
alga
algebra

$ egrep '^(.)(.)((.)\4)?\2\1$' /usr/share/dict/words | head
 # Find 4-6 letter palindromes
deed
noon
peep
poop
redder
sees
toot
```

### Alternative matches



```bash
$ egrep '^(ab|no).*(ly|ne)$' /usr/share/dict/words
ably
abnormally
aborigine
abruptly
absolutely
absurdly
abundantly
nobly
noiselessly
...

```



### Linux kernel source code directory

##### Back to grep

```bash
$ mkdir section2-5 && cd section2-5
$ curl -Ls  https://mirrors.edge.kernel.org/pub/linux/kernel/v1.0/linux-1.0.tar.gz |  tar -xzvf -
$ cd linux/kernel
$ grep -l stdarg.h *.c
# List C files containing stdarg.h
panic.c
printk.c
vsprintf.c
```

```bash
    $ cd ../fs
 # Change to filesystem source code directory
$ grep -rl kernel.h . | head -5
# Search recursively
./block_dev.c
./buffer.c
./exec.c
./ext/dir.c
./ext/file.c

```

#### Complement matches


```bash
$ egrep '^[ ]*(/\*|\*|\*/)' *.c | head -10
# List comment lines
binfmt_coff.c:/*
binfmt_coff.c: * These are the functions used to load COFF IBSC binfmt_coff.c: * Information on COFF format may be obtained in  binfmt_coff.c: * Compatibility Specification 2 or O'Rilley's book binfmt_coff.c: * libraries are defined only the in the Intel book.
binfmt_coff.c: *
binfmt_coff.c: * This file is based upon code written by Eric 
binfmt_coff.c: * file format.
binfmt_coff.c: */
```

```bash 
$ egrep -v '^[ ]*(/\*|\*|\*/)' *.c | head -10
 # List non-comment lines
  egrep -v '^[ ]*(/\*|\*|\*/)' *.c | head -10
binfmt_coff.c:
binfmt_coff.c:#include <linux/fs.h>
binfmt_coff.c:#include <linux/sched.h>
binfmt_coff.c:#include <linux/mm.h>
binfmt_coff.c:#include <linux/mman.h>
binfmt_coff.c:#include <linux/a.out.h>
binfmt_coff.c:#include <linux/errno.h>
binfmt_coff.c:#include <linux/signal.h>
binfmt_coff.c:#include <linux/binfmts.h>
binfmt_coff.c:#include <asm/segment.h>
```



### Search for fixed strings

```bash
$ fgrep OK *.c | head -5
# Fixed string grep
binfmt_elf.c:   /* OK, we are done with that, now set up the arg stuff,
binfmt_elf.c:   /* OK, This is the point of no return */
buffer.c:/* OK, FINALLY we know that this buffer is the only one... */
exec.c:          * OK, we've parsed out the interpreter name and
exec.c:          * OK, now restart the process with the ...

$  fgrep -c OK *.c
binfmt_coff.c:0
binfmt_elf.c:2
block_dev.c:0
buffer.c:1
devices.c:0
exec.c:3
fcntl.c:0
fifo.c:0
file_table.c:0
filesystems.c:0
...

$ fgrep -c OK *.c | 
> while read -r line;
>  do 
>  n=$(echo $line | cut -f 2 -d :); 
>  if [ $n -ge 1 ]; then
>    echo $line; 
>  fi;
>  done
binfmt_elf.c:2
buffer.c:1
exec.c:3
open.c:1

```