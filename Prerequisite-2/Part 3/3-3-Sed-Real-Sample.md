### Generate commands

```bash
$ cd 
$ cd section3-2
$ cat > files <<\EOF
>contact-de
>faq-de
>index-de
>news-de
>products-de
>contact-en
>faq-en
>index-en
>news-en
>products-en
>contact-fr
>faq-fr
>index-fr
>news-fr
>products-fr
>EOF

$ for file in $(cat files) ; do
> $(echo $file > "$file.html");
> done

$ ls 
$ mkdir en de fr
 # Create one directory for each language
```



##### move  every file to its corresponding folder 

```bash
$ ls |
> sed -n 's/\([^-]*\)-\(..\)\.html/mv \1-\2.html \2\/\1.html/p'

mv contact-de.html de/contact.html
mv contact-en.html en/contact.html
mv contact-fr.html fr/contact.html
mv faq-de.html de/faq.html
mv faq-en.html en/faq.html
mv faq-fr.html fr/faq.html
mv index-de.html de/index.html
mv index-en.html en/index.html
mv index-fr.html fr/index.html
.....

$ ls | sed -n 's/\([^-]*\)-\(..\)\.html/mv \1-\2.html \2\/\1.html/p' | sh

$ ls
BSD  EOF.html  de  en  files  fr  song.txt
$ ls en
contact.html  faq.html  index.html  news.html  products.html 
```
