#pico2022 #forensics 

## Challenge:
```md
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download compressed disk image](https://artifacts.picoctf.net/c/330/disk.flag.img.gz)
```

## Process:
Download the image.
```bash
curl -O https://artifacts.picoctf.net/c/330/disk.flag.img.gz 
```
#curl 

Uzip the file.
```bash
gzip -d disk.flag.img.gz
```
#gz #gzip 

Let's look at the *img*.
```
mmls disk.flag.img
```
#mmls 

```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```

Let's look at that last partition. I did a little googling and saw ```fls```.
```bash
man fls
```
#man #fls

From the *man* page.
```
fls - List file and directory names in a disk image.
...
-o imgoffset
	The sector offset where the file system starts in the image.
```
#fls 

So I run:
```bash
fls -o 360448 disk.flag.img
```
#fls 

```
d/d 451:	home
d/d 11:	lost+found
d/d 12:	boot
d/d 1985:	etc
d/d 1986:	proc
d/d 1987:	dev
d/d 1988:	tmp
d/d 1989:	lib
d/d 1990:	var
d/d 3969:	usr
d/d 3970:	bin
d/d 1991:	sbin
d/d 1992:	media
d/d 1993:	mnt
d/d 1994:	opt
d/d 1995:	root
d/d 1996:	run
d/d 1997:	srv
d/d 1998:	sys
d/d 2358:	swap
V/V 31745:	$OrphanFiles
```
#fls 

And looking at the *root*.
```
fls -o 360448 disk.flag.img 1995
```
#fls 

```
r/r 2363:	.ash_history
d/d 3981:	my_folder
```
#fls 

And what's in the *my_folder* directory?
```bash
fls -o 360448 disk.flag.img 3981
```
#fls 

```
r/r * 2082(realloc):	flag.txt
r/r 2371:	flag.uni.txt
```
#fls 


After a quick google.
```bash
man icat
```
#man #icat

```
icat - Output the contents of a file based on its inode number.
```
#icat 

Looking at the files.
```bash
icat -o 360448 disk.flag.img 2371
```
#icat

That gives me the flag.
```
icat -o 360448 disk.flag.img 2371 > flag.txt
```
#icat 

**Flag: *picoCTF{by73_5urf3r_3497ae6b}***
