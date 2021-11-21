

### Repository fetching

$

```
 git clone https://github.com/torvalds/linux.git
 # Clone the Linux repo
```

Cloning into 'linux'... remote: Counting objects: 4478865, done. remote: Compressing objects: 100% (482/482), done. remote: Total 4478865 (delta 397), reused 129 (delta 129), pack-reused 4478253 Receiving objects: 100% (4478865/4478865), 1.27 GiB | 11.51 MiB/s, done. Resolving deltas: 100% (3734690/3734690), done. Checking connectivity... done. Checking out files: 100% (52221/52221), done. $

```
 cd linux
```

$

```
 git log v5.6-rc2 | head -12
 # List commits
```

commit 11a48a5a18c63fd7621bb050228cebf13566e4d8 Author: Linus Torvalds <torvalds@linux-foundation.org> Date:   Sun Feb 16 13:16:59 2020 -0800     Linux 5.6-rc2 commit ab02b61f24c76b1659086fcc8b00cbeeb6e95ac7 Merge: 44024adb4aab e0354d147e58 Author: Linus Torvalds <torvalds@linux-foundation.org> Date:   Sun Feb 16 13:05:46 2020 -0800     Merge tag 'for-linus-5.6-1' of https://github.com/cminyard/linux-ipmi $

### Commit log

$

```
 git log --pretty=format:%an |
 # List author name of each commit
```

\>

```
 grep -v Torvalds |
 # Omitting Linus Torvalds
```

\>

```
 head
 # First ten
```

Peter Zijlstra Qais Yousef Dmitry V. Levin Junxiao Bi Chen Jie Seth Jennings Hugh Dickins Mike Kravetz Naoya Horiguchi Chris Wilson $

### Process the commit log

$

```
 git log --pretty=format:%ae |
 # List each commit's author email
```

\>

```
 sort |
 # Bring emails together
```

\>

```
 uniq -c |
 # Count occurrences
```

\>

```
 sort -rn |
 # Order by number
```

\>

```
 head
 # List first ten
```

  16101 torvalds@linux-foundation.org   6078 davem@davemloft.net   5582 tiwai@suse.de   3948 broonie@opensource.wolfsonmicro.com   3865 viro@zeniv.linux.org.uk   3844 hsweeten@visionengravers.com   3518 mingo@elte.hu   3172 tglx@linutronix.de   2835 arnd@arndb.de   2739 joe@perches.com $

### Obtain details for each file

$

```
 find kernel -type f -print |
 # Find kernel source code files
```

\>

```
 while read f ; do
 # For each file
```

\>

```
   echo -n "$f "
 # Print its name on a single line
```

\>

```
   git log --oneline $f | wc -l
 # Count number of changes
```

\>

```
 done |
```

\>

```
 head -3
 # Print first three entries
```

kernel/.gitignore 5 kernel/acct.c 89 kernel/async.c 34 $

```
 find kernel -type f -print |
```

\>

```
 while read f ; do
```

\>

```
   echo -n "$f "
```

\>

```
   git log --oneline $f | wc -l
```

\>

```
 done |
```

\>

```
 sort -k 2nr |
 # Sort by the second field in reverse numerical order
```

\>

```
 head
```

kernel/trace/trace.c 811 kernel/cgroup.c 807 kernel/fork.c 686 kernel/sched/core.c 647 kernel/workqueue.c 529 kernel/sysctl.c 513 kernel/exit.c 509 kernel/trace/ftrace.c 476 kernel/sched/fair.c 474 kernel/signal.c 457 $

### Obtain details for each line

$

```
 git blame kernel/fork.c | sed -n 20,40p
 # List attribution of lines 20-40
```

8703e8a465b1e (Ingo Molnar                    2017-02-08 18:51:30 +0100   20) #include <linux/sched/user.h> 6a3827d7509cb (Ingo Molnar                    2017-02-08 18:51:31 +0100   21) #include <linux/sched/numa_balancing.h> 03441a3482a31 (Ingo Molnar                    2017-02-08 18:51:35 +0100   22) #include <linux/sched/stat.h> 299300258d1bc (Ingo Molnar                    2017-02-08 18:51:36 +0100   23) #include <linux/sched/task.h> 68db0cf106786 (Ingo Molnar                    2017-02-08 18:51:37 +0100   24) #include <linux/sched/task_stack.h> 32ef5517c2980 (Ingo Molnar                    2017-02-05 11:48:36 +0100   25) #include <linux/sched/cputime.h> b3e5838252665 (Christian Brauner              2019-03-27 13:04:15 +0100   26) #include <linux/seq_file.h> 037741a6d4ab2 (Ingo Molnar                    2017-02-03 10:08:30 +0100   27) #include <linux/rtmutex.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   28) #include <linux/init.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   29) #include <linux/unistd.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   30) #include <linux/module.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   31) #include <linux/vmalloc.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   32) #include <linux/completion.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   33) #include <linux/personality.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   34) #include <linux/mempolicy.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   35) #include <linux/sem.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   36) #include <linux/file.h> 9f3acc3140444 (Al Viro                        2008-04-24 07:44:08 -0400   37) #include <linux/fdtable.h> da9cbc8739530 (Jens Axboe                     2008-06-30 20:42:08 +0200   38) #include <linux/iocontext.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   39) #include <linux/key.h> ^1da177e4c3f4 (Linus Torvalds                 2005-04-16 15:20:36 -0700   40) #include <linux/binfmts.h> $

### Process blame details

$

```
 git blame --line-porcelain kernel/fork.c | head -15
```

1da177e4c3f41524e886b7f1b8a0c1fc7321cac2 1 1 13 author Linus Torvalds author-mail <torvalds@ppc970.osdl.org> author-time 1113690036 author-tz -0700 committer Linus Torvalds committer-mail <torvalds@ppc970.osdl.org> committer-time 1113690036 committer-tz -0700 summary Linux-2.6.12-rc2 boundary filename kernel/fork.c        /* 1da177e4c3f41524e886b7f1b8a0c1fc7321cac2 2 2 author Linus Torvalds $

### Who knows best this file?

$

```
 git blame --line-porcelain kernel/fork.c |
 # Obtain line metadata
```

\>

```
 grep '^author ' |
 # Show each line's author
```

\>

```
 sort |
 # Order by author
```

\>

```
 uniq -c |
 # Count author instances
```

\>

```
 sort -rn |
 # Order by count
```

\>

```
 head
 # Show first ten
```

​    572 author Linus Torvalds    207 author Oleg Nesterov    135 author JANAK DESAI     95 author Al Viro     67 author Eric W. Biederman     59 author Heinrich Schuchardt     58 author Ingo Molnar     53 author Konstantin Khlebnikov     48 author Kees Cook     47 author Thomas Gleixner $

### Average age of file's lines

$

```
 date +%s
 # Show date in seconds since Epoch (1/1/1970)
```

1582286183 $

```
 date -d @1582286183
 # Print the date for this number of Epoch seconds
```

Fri, Feb 21, 2020 13:56:23 $

```
 date -d @0
 # Print the date at Epoch
```

Thu, Jan 01, 1970  2:00:00 AM $

```
 date -d @$(
 # Print the date corresponding to the output of:
  git blame --line-porcelain kernel/fork.c |
  awk '/^author-time / {sum += $2; count++}
 # Maintain sum and count of commit times
    END {printf("%d", sum / count)}'
 # Print mean authorship time
)
```

Tue, Aug 20, 2013 20:42:48 $

### Track file size growth

$

```
 file=drivers/thermal/of-thermal.c
 # File to examine
```

$

```
 git log --pretty=format:%H -n 3 $file
 # Show SHA of commits
```

285249884ec19480f99c011d223760bb1fc865a2 17e8351a77397e8a83727eb17e3a3e9b8ab5257a $

```
 git log --pretty=format:%H $file |
 # Obtain commits' SHA
```

\>

```
 while read sha ; do
 # For each SHA
```

\>

```
   git show $sha:$file |
 # List file state at that commit
```

\>

```
   wc -l
 # Count number of lines
```

\>

```
 done |
```

\>

```
 head -15
 # First 15 entries
```

988 988 988 966 962 958 957 954 954 930 908 923 902 881 886