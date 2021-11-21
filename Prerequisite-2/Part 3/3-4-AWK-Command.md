### AWK Basics

```bash
$ mkdir section4-4 && cd section4-4
$ cat > employee.txt <<\EOF
1001 John sena 40000
1002 Jafar Iqbal   60000
1003 Meher Nigar   30000
1004 Jonny Liver   70000
EOF

$ awk '{ printf  "%10s\n", $1 }' employee.txt
      1001
      1002
      1003
      1004
$ awk '{ print $1 }' FS='\t' input.txt


$ cat > customer.csv <<\EOF
Id, Name, email, phone
1, Sophia, sophia@yahoo.com, (862) 478-7263
2, Amelia, amelia@gmail.com, (530) 764-8000
3, Emma, emma@hotmail.com, (542) 986-2390
EOF

$ awk -F "," '{print $2}' customer.csv
 Name
 Sophia
 Amelia
 Emma

$ awk  -F "," 'NR > 1 {print "Name:" $2 ", Email:" $3 ", Phone:" $4}' customer.csv
Name: Sophia, Email: sophia@yahoo.com, Phone: (862) 478-7263
Name: Amelia, Email: amelia@gmail.com, Phone: (530) 764-8000
Name: Emma, Email: emma@hotmail.com, Phone: (542) 986-2390

$ cat > items.txt  <<\EOF
HDD  Samsung   $100
Mouse  A4Tech
Printer   HP   $200
EOF

$  awk '{ if ($3 == "") print "Price field is missing in line " NR }'  items.txt
Price field is missing in line 2



$ cat > awkcsv.awk <<EOF
BEGIN {FS = ","} {printf "%5s(%s)\n", $2,$1}
EOF

$ awk -f awkcsv.awk customer.csv
 Name(Id)
 Sophia(1)
 Amelia(2)
 Emma(3)
```


##### AWK Regex 
 ```bash
$ echo -e "Linux is free to use\n It is an open-source software\nLinuxHint is a popular blog site" | 
> awk '/^Linux/'

Linux is free to use
LinuxHint is

 ```

##### AWK as programming language 

```bash
$ cat > area.awk  <<\EOF
# Calculate area
function area(height,width){
return height*width
}
# Starts execution
BEGIN {
print "Enter the value of height:"
getline h < "-"
print "Enter the value of width:"
getline w < "-"
print "Area = " area(h,w)
}
EOF

$  awk -f area.awk

```

#####  A Real Sample

```bash
$ curl -Ls https://mirrors.edge.kernel.org/pub/linux/kernel/v1.0/linux-1.0.tar.gz |
> tar -tzvf - > contents.txt
# Fetch Linux kernel
$ head contents.txt
drwxr-xr-x root/root         0 1994-03-14 01:20 linux/
-rw-r--r-- root/root      6891 1994-03-14 02:08 linux/Makefile
drwxr-xr-x root/root         0 1994-03-13 22:09 linux/boot/
-rw-r--r-- root/root      9187 1993-12-01 16:14 linux/boot/bootsect.S
-rw-r--r-- root/root     17689 1993-12-01 16:14 linux/boot/setup.S
-rw-r--r-- root/root      8651 1994-02-03 14:07 linux/boot/head.S
drwxr-xr-x root/root         0 1994-03-13 22:09 linux/fs/
-rw-r--r-- root/root      4832 1993-12-01 16:14 linux/fs/stat.c
-rw-r--r-- root/root      1835 1993-12-21 14:00 linux/fs/Makefile
-rw-r--r-- root/root      2513 1993-12-01 16:14 linux/fs/read_write.c

$ awk '
> { size += $3; n++ }
> # Sum size and number of files
> END {
> # Print summmary
> print "Total size " size
> print "Number of files " n
> print "Average file size " size / n
> }
>' contents.txt

Total size 4719743
Number of files 595
Average file size 7932.34
```

```bash
$  echo "/user/bin/t.txt" | awk '{ print $1; sub(".*/","",$1); print $1;}'
/user/bin/t.txt
t.txt

$ awk '
> {
> sub(".*/", "", $6)
> # Remove path
> if (!sub(".*\\.", "", $6))
> # Keep only extension
>    next
> # Skip files without extension
> size[$6] += $3
# Tally size of extension
> }
> END {
> for (i in size)
>   print i, size[i]
>   }' contents.txt  |
>  sort -k 2nr |
>  head

```


