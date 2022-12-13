#pico2022 #forensics 

## Challenge:
```md
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
```

This challenge launches an instance.
```md
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download disk image](https://artifacts.picoctf.net/c/373/disk.img.gz)
-   Remote machine: `ssh -i key_file -p 62501 ctf-player@saturn.picoctf.net`
```

## Process:
I first download the disk image.
```bash
curl -O https://artifacts.picoctf.net/c/373/disk.img.gz
```
#curl 

Then I unzip the image.
```bash
gzip -d disk.img.gz
```
#gz #gzip 

I ran *mmls*.
![[046_Operation_Oni-0.png]]
#mmls 

And looked for *OPENSSH PRIVATE KEY*.
![[046_Operation_Oni-1.png]]
#strings #grep 

Then some maths on this.

Multiply by 512 (bytes in sector).
```bash
expr 206848 \\*  512
```
#expr

```
105906176
```

Subtract this from where the *OPENSSH PRIVATE KEY* begins to find an offset.
```bash
expr 114562048 - 105906176
```
#expr

```
8655872
```

Divide this by the block size.
```bash
expr 8655872 / 1024
```
#expr 

```
8453
```

Then use that result to find the inode number.
```bash
ifind -f ext4 -o 206848 -d 8453 disk.img
```
#ifind

```
15
```

Then print the contents of the file.
```bash
icat -f ext4 -o 206848 disk.img 15
```
#icat 

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACCCLR0HD7N0U/aOCIfE8hu37rqZXPVlAw2nZTCsXzW5iwAAAJhPAhe3TwIX
twAAAAtzc2gtZWQyNTUxOQAAACCCLR0HD7N0U/aOCIfE8hu37rqZXPVlAw2nZTCsXzW5iw
AAAEC64hkpckRMk5Jy2dRmcBTSoQvavri0nLhU6aqeGBT1OIItHQcPs3RT9o4Ih8TyG7fu
uplc9WUDDadlMKxfNbmLAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

I saved this output to a file named *key_file*.

Then remote into the server.
```bash
ssh -i key_file -p 62501 ctf-player@saturn.picoctf.net
```
#ssh

And then just *ls* to see the files. Then *cat* the *flag.txt* file to get the flag.
![[046_Operation_Oni-2.png]]
#ls #cat 

There's the flag.
```bash
echo "picoCTF{k3y_5l3u7h_b5066e83}" > flag.txt
```
#echo 

**Flag: *picoCTF{k3y_5l3u7h_b5066e83}***
