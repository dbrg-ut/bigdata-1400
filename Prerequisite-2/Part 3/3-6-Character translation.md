### Character translation


```bash
$ echo 'This is a test' | tr ' ' -

This-is-a-test 

$ echo 'This is a test' | tr a-z A-Z

THIS IS A TEST $

$ echo 'meet me by the entrance at midnight' >message

$ tr a-z l-za-k <message |
# Simple substitution cipher
> tee secret
# Keep a copy of the secret message

xppe xp mj esp pyeclynp le xtoytrse 

$ tr l-za-k a-z <secret
meet me by the entrance at midnight 
```

### Spell checking

```bash
$ curl -s --compressed https://www.gutenberg.org/cache/epub/1342/pg1342.txt >pride-and-prejudice.txt

$ tr -c a-zA-Z '\n' <pride-and-prejudice.txt |
# Convert non-word characters to newlines
> head -1
The Project Gutenberg EBook of Pride and 

$ tr -c a-zA-Z '\n' <pride-and-prejudice.txt |
# Convert non-word characters to newlines
> tr A-Z a-z |
# Convert uppercase to lowercase
> head

the project gutenberg ebook of pride and $

$ tr -c a-zA-Z '\n' <pride-and-prejudice.txt |
# Convert non-word characters to newlines
> tr A-Z a-z |
# Convert uppercase to lowercase
> sort |
# Sort text's words
> uniq |
# Remove duplicates
> head

a abatement abhorrence abhorrent abide abiding abilities able ablution 

