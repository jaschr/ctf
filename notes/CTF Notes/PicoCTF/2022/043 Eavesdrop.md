#pico2022 #forensics 

## Challenge:
```md
Download this packet capture and find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/358/capture.flag.pcap)
```

## Process:
Download the packet.
```bash
curl -O https://artifacts.picoctf.net/c/358/capture.flag.pcap
```
#curl 

I opened the packet in *wireshark* and followed the TCP stream.
![[043_Eavesdrop-0.png]]
#wireshark 

I see the conversation talks about the command:
```
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
```
#openssl 

And in the other TCP Stream I found  *Salted_*.
![[043_Eavesdrop-1.png]]
#wireshark 

I exported the bytes: ```File > Export Packet Bytes``` and saved the bytes to *bytes.des3*. After this I modified the given command and ran it.
```bash
openssl des3 -d -salt -in bytes.des3 -out flag.txt -k supersecretpassword123
```
#openssl

This gave me the flag!

**Flag: *picoCTF{nc_73115_411_5786acc3}***
