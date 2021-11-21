####  Grep Basics

###### Begin/End of a string

```bash
$ grep ali /usr/share/dict/words 
abnormalities
abnormality
abnormality's
actualities
actuality
actuality's
alias
alias's
....

$ grep '^ali' /usr/share/dict/words
alias
alias's
aliased
aliases
aliasing
alibi
alibi's
alibied
alibiing
....

$ grep 'ali$' /usr/share/dict/words
alkali

```



##### Special Chars 

```bash
$ grep 'a.a.a' /usr/share/dict/words
adamant
adamant's
avalanche
avalanche's
avalanches
banana
banana's
bananas
camaraderie
camaraderie's
caravan
....

$ grep '^t.y$' /usr/share/dict/words
thy
toy
try

##### All 4 letters Words
$ grep '^....$' /usr/share/dict/words | wc -l
1946

$ grep '^k.*d.*d$' /usr/share/dict/words
keyboarded
kidded
kidnaped
kidnapped
kindled
kindred
kneaded


```



##### Set of Characters

```bash
$ grep '^[A-Z]' /usr/share/dict/words | wc -l
245

$ grep '^d.[rtsf].d$' /usr/share/dict/words
dared
dated
dosed
doted

$ grep '[^a-zA-Z]' /usr/share/dict/words | head
African's
Allah's
American's
Americanism's
April's
Asian's
August's
B's
British's
C's

$ echo "Hello World" | grep '\b[A-Z]'
Hello World
```



##### Grep Special Classes

```bash
$ find /mnt/c -maxdepth 1 -type d | grep '[[:space:]]'
/mnt/c/Program Files
/mnt/c/Program Files (x86)
/mnt/c/System Volume Information

$ grep '[[:punct:]]' /usr/share/dict/words

```

- [[:digit:]]
- [[:blank:]]
- [[:print:]]
- [[:xdigit:]]