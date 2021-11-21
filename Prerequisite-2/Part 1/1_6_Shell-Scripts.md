### Wildcard expansion

```bash
$ mkdir stores
$ cd stores
$ touch storeone.a storetwo.b storethree.c storeplain anotherstore
$ echo *
anotherstore storeone.a storeplain storethree.c storetwo.b
$ echo store*
# Match files beginning with store
storeone.a storeplain storethree.c storetwo.b
echo *.?
# ... ending in . with a single character
storeone.a storethree.c storetwo.b $
$ echo store*.[ab]
 # ... ending in .a or .b
$ storeone.a storetwo.b 
$ echo store*.[a-z]
storeone.a storethree.c storetwo.b
$ find store*.[a-z]
 # ... ending in . followed by a lowercase letter
storeone.a
storethree.c
storetwo.b
$ echo store*.[^b]
 # ... ending in . followed by anything but b
storeone.a storethree.c
$ find store*.[^b]
storethree.c
```


### Shell variables

we can define variables in command line. 

```bash
$ name=Ali
# Assign name to variable
$ name = Ali # Error
$ name= Ali # Error
$ surname=Karimi
echo $name
# Expand variable
Ali
```


#### Built-in variable
```bash
echo $PATH
 # Built-in variable (executable file path)
 /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/mnt/c/Python39/Scripts/:....

$ echo $HOME
 # Built-in variable (home directory path)
/home/mojtaba $
$ cd $HOME/stores
```


#### Read into variables four words

```bash
$ read a b c d
Live free or die! 
$ echo $a:$b:$c:$d
live:free:or:die!
```

#### Unwanted expansion here
```bash
$ echo This pen costs $4.99
This pen costs .99 
### Escape expansion
#Option 1 : Use '' to Protect whole content
$ echo 'This pen costs $4.99'
This pen costs $4.99 

```
- *Hint* :  *Only **Single Quotation Marks** works here .*

```bash
### Option 2 :  using Escape Character
$ echo The pen\'s cost is \$4.99
 # Protect single characters
The pen's cost is $4.99 

$ echo "*** Meet $name's father ****"
 # Expand variables
*** Meet Ali's father **** 

$  echo "\"$name $surname\" paid \$4.99"
# Expand and protect

$ echo 'No backspaces (\) here. Go out of '\'' and use them.'
No backspaces (\) here. Go out of ' and use them. $

#### Multi Line Statements
$  echo 'A multi line string
>  ends here.
>  '
A Multi Line
ends here

```



### Command expansion


```bash
 $ echo "Today is $(date)"
 # Expand command
 Today is Wed Dec 23 18:40:34 +0330 2020
```



```bash
$ start=$(date +%s)
 # Assign the result to a variable
$ echo $start
1608736325
$ sleep 10
end=$(date +%s)
echo "The process lasted $(expr $end - $start) seconds"
The process lasted 13 seconds 
```

### Here documents

```
$ cat -n <<\EOF
 Two roads diverged in a yellow wood,
 And sorry I could not travel both
 And be one traveler, long I stood
 And looked down one as far as I could
 To where it bent in the undergrowth;
 EOF


1  Two roads diverged in a yellow wood,     
2  And sorry I could not travel both     
3  And be one traveler, long I stood     
4  And looked down one as far as I could     
5  To where it bent in the undergrowth; 
```
#### First Shell Scripts

```bash
cat > sleep.sh <<\End
> start=$(date +%s)
> echo $start
> sleep 10
> end=$(date +%s)
> echo "The process lasted $(expr $end - $start) seconds"
> End

$ cat sleep.sh
start=$(date +%s)
echo $start
sleep 10
end=$(date +%s)
echo "The process lasted $(expr $end - $start) seconds"
```

#### Executing the shell script

###### Option 1 : using sh
```bash
$ sh sleep.sh
1608737063
The process lasted 10 seconds
```
###### Option 2 : using hash bang (SheBang)
```bash
$ ls -lh sleep.sh
-rw-r--r-- 1 mojtaba mojtaba 111 Dec 23 18:52 sleep.sh
$ chmod +x sleep.sh
$ ls -lh sleep.sh
-rwxr-xr-x 1 mojtaba mojtaba 111 Dec 23 18:52 sleep.sh
$ nano sleep.sh
# add #!/bin/sh at the very begining of the file
# ctrl+s / ctrl+x
$ sleep.sh #Error 
sleep.sh: command not found 
# when file path is ommited, shell searches in PATH variable not the current directory
$ ./sleep.sh
1608737791
The process lasted 10 seconds
```

###### Reading Time to Sleep from input
```bash
$ nano sleep.sh
$ cat sleep.sh
#!/bin/sh
echo "This File Called With $# Parameters"
start=$(date +%s)
echo $start
sleep $1
end=$(date +%s)
echo "The process lasted $(expr $end - $start) seconds"

$ ./sleep.sh 5
This File Called With 1 Parameters
1608738024
The process lasted 5 seconds

```

