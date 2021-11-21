### The command line prompt

```bash
$ echo hello world!
```

Hello World! 

```bash
$ echo a b
```

a b 

```bash
$ date
```

Fri 21 Feb 2020 01:04:36 PM EET 



### Editing

```bash
$ touch a-file
```

```
$ touch a-file-with-a-longer-name
```

```bash
$ ls
```

a-file  a-file-with-a-longer-name 

### Enter long file names



```bash
 $ touch really-long-file-name
```



```bash
$ ls
```

really-long-file-name 

```bash
$ touch really-long-file-name
```



### Interrupt execution



```bash
$ sleep 60
# Wait for 60 seconds
```

$ ^C 

### Command options



```bash
$ touch a
```



```bash
$ touch b
```



```bash
$ ls
```

a  b 

```bash
 ls -l
 # Specify option to list files in long format
 total 0 
 -rw-r--r-- 1 dds None 0 Dec  7 10:33 a
 -rw-r--r-- 1 dds None 0 Dec  7 10:33 b 
```



```bash
 ls -r
 # Specify option to list files in reverse order
```

b  a 

```bash
 ls --reverse
 # Same option in long format
```

b  a 

```bash
$ ls -l -r
 # Specify two short options
 total 0 
-rw-r--r-- 1 dds None 0 Dec  6 10:33 b 
-rw-r--r-- 1 dds None 0 Dec  6 10:33 a 
```



```bash
$ ls -lr
 # Combine two short options
 total 0 
-rw-r--r-- 1 dds None 0 Dec  6 10:33 b 
-rw-r--r-- 1 dds None 0 Dec  6 10:33 a 
```


```bash
$ touch -t 200408132045 olympic-opening
 # Specify short option with argument
```



```bash
 $ touch --date=2004-08-13T20:45 olympic-opening
 # Long option with argument
```



```bash
$ ls -l
```

-rw-r--r-- 1 dds None 0 Aug 13  2004 olympic-opening 

### Get help 

```bash
 $ man ls
```

### Built-in help

```bash
 $ sleep --help
```



### Info - Full Guide

```bash
$ info wc
$ info sort
```