####  Cut/Sed /AWK

```bash
 $ head -5 /etc/passwd
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync 

$ cut -d: -f 1 /etc/passwd | head -5
# Output field 1
root
daemon
bin
sys
sync

$ cut -d: -f 3-5 /etc/passwd | head -5
# Output fields 3-4
0:0:root
1:1:daemon
2:2:bin
3:3:sys
4:65534:sync
```



### Conditional selection with awk

```bash
$ awk '/bash/' /etc/passwd
# Output lines containing "bash"
mojtaba:x:1000:1000:,,,:/home/mojtaba:/usr/bin/bash
test:x:1001:1001::/home/test:/usr/bin/bash
editor:x:1003:1003:Editor,,,:/home/editor:/bin/bash

$ awk -F: '$3 > 1000' /etc/passwd
 # Lines where field 3 > 1000
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
test:x:1001:1001::/home/test:/usr/bin/bash
test20:x:1002:1002::/home/test20:/bin/sh
editor:x:1003:1003:Editor,,,:/home/editor:/bin/bash

$ awk -F: '{print $1}' /etc/passwd | head -5
# Output field 1
root
daemon
bin
sys
sync

$  awk -F: '$3 > 1000 {print $1}' /etc/passwd | head -5
nobody
test
test20
editor

$ awk '!/^#/ {print $1}' /etc/services | head
 # Combine predicate and action
tcpmux
echo
echo
discard
discard
systat
daytime
daytime
netstat
```


### RE selection with sed

```bash
$ mkdir section2-7 && cd section2-7
$ curl -Ls  https://mirrors.edge.kernel.org/pub/linux/kernel/v1.0/linux-1.0.tar.gz |  tar -xzvf -
$ cd linux/kernel
$ # Linux kernel source code directory
$ find *.c . | head -5
dma.c
exit.c
fork.c
info.c
ioport.c
$ head -10 dma.c
/* $Id: dma.c,v 1.5 1992/11/18 02:49:05 root Exp root $
 * linux/kernel/dma.c: A DMA channel allocator. Inspired by linux/kernel/irq.c.
 * Written by Hennus Bergman, 1992.
 */

#include <linux/kernel.h>
#include <linux/errno.h>
#include <asm/dma.h>

$ sed -n 's/#include *["<]\([^">]*\).*/\1/p' *.c | head
 # Output included file names

linux/kernel.h
linux/errno.h
asm/dma.h
linux/wait.h
linux/errno.h
linux/signal.h
linux/sched.h
linux/kernel.h
linux/resource.h
linux/mm.h
```



### Select which lines to process

```bash
$ cd /usr/share/dict
# Output lines from lines 1000 to 1005
$ sed -n 1000,1005p words
advisories
advisors
advisory
advisory's
advocate
advocate's

```