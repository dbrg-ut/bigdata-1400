#### Stream Editor

***syntax***  :  **sed** [options] commands [file-to-edit | input from pipeline ] 

```bash
$ cd
$ mkdir section3-2 && cd section3-2
$ cp /usr/share/common-licenses/BSD .
$ cat BSD
Copyright (c) The Regents of the University of California.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
```

#### Sed Basics

```bash
$ sed '' BSD
Copyright (c) The Regents of the University of California.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
.....

$ cat BSD | sed ''
### Same As Above

```



##### Printing Lines

```bash
$ sed 'p' BSD
Copyright (c) The Regents of the University of California.
Copyright (c) The Regents of the University of California.
All rights reserved.
All rights reserved.

$ sed -n 'p' BSD
Copyright (c) The Regents of the University of California.
All rights reserved.

....
```



##### Address Range/ Delete command

```bash
$ sed -n '1p' BSD
Copyright (c) The Regents of the University of California.

$ sed -n '1,5p' BSD
Copyright (c) The Regents of the University of California.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions

$ sed -n '4,+2p' BSD
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

$ sed '1,6d' BSD
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright 

$ sed -i.bak '1,6d' BSD
$ ls 
BSD  BSD.bak
$ mv BSD.bak  BSD
```



##### Substituting Text

*'s/old_word/new_word/'*

```bash
$ echo "One Day" | sed 's/Day/Night/'
One Night
$ echo "sunday is a  pleasant day" | sed 's/day/night/'
sunnight is a  pleasant day
$ echo "sunday is a  pleasant day" | sed 's/day/night/2'
sunday is a  pleasant night
$ echo "sunday is a  pleasant day" | sed 's/day/night/g'
sunnight is a  pleasant night
$  echo "http://www.example.com/index.html" | sed 's_com/index_org/home_'
http://www.example.org/home.html
```



```bash
echo "this is the song that never ends
yes, it goes on and on, my friend
some people started singing it
not knowing what it was
and they'll continue singing it forever
just because..." > song.txt

$ sed -n 's/on/forward/2p' song.txt
yes, it goes on and forward, my friend

$  sed -n 's/SINGING/saying/ip' song.txt
some people started saying it
and they'll continue saying it forever

$ sed -n 's/ed\s/ED /p' song.txt
some people startED singing it

$ sed -n 's/\bw/W/gp' song.txt
not knowing What it Was

$ sed -n '5!s/it/It/pg' song.txt
yes, It goes on and on, my friend
some people started singing It
not knowing what It was

$ echo "HI, it's 12" | sed -n '/[0-9]\{2\}/p'
HI, it's 12
$ echo "     Hi" | sed 's/^[ ]*//'
Hi
$  sed 10q file.txt
# Head replcement

$ sed -n 's/\/bin\/bash/\/bin\/csh/p' /etc/passwd
$  sed -n 's@/bin/bash@/bin/csh@p' /etc/passwd
mojtaba:x:1000:1000:,,,:/home/mojtaba:/usr/bin/csh
test:x:1001:1001::/home/test:/usr/bin/csh
editor:x:1003:1003:Editor,,,:/home/editor:/bin/csh


   
```



##### Replacing and Referencing Matched Text

```bash
$ sed 's/^.*at/REPLACED/' song.txt
REPLACED never ends
yes, it goes on and on, my friend
some people started singing it
REPLACED it was
and they'll continue singing it forever
just because...

$  sed 's/^.*at/(&)/' song.txt
(this is the song that) never ends
yes, it goes on and on, my friend
some people started singing it
(not knowing what) it was
and they'll continue singing it forever
just because...

$  sed 's/\([a-zA-Z0-9][a-zA-Z0-9]*\) \([a-zA-Z0-9][a-zA-Z0-9]*\)/\2 \1/' song.txt
is this the song that never ends
yes, goes it on and on, my friend
people some started singing it
knowing not what it was
they and'll continue singing it forever
because just...

$  sed 's/\([^ ][^ ]*\) \([^ ][^ ]*\)/\2 \1/' song.txt
is this the song that never ends
it yes, goes on and on, my friend
people some started singing it
knowing not what it was
they'll and continue singing it forever
because... just

$  sed -n '1,10s/\([^:]*\).*/\1/p' /etc/passwd
root
daemon
bin
sys
sync
games
man
lp
mail
news

$ sed 's/^\([1-9]\+\)\./\1\)/' BSD
...
are met:
1) Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2) Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3) Neither the name of the University nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.
   

```





