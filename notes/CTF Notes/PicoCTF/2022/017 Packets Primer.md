#pico2022 #forensics 

## Challenge:
```md
Download the packet capture file and use packet analysis software to find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/199/network-dump.flag.pcap)
```

## Process:
I first *wget* the packet capture file.
```bash
wget -q https://artifacts.picoctf.net/c/199/network-dump.flag.pcap
```
#wget 

The challenge recommends installing *Wireshark*.
```bash
sudo apt install wireshark
```
#sudo #apt #wireshark

I first tried *strings* on the file. Which gave me the flag. I am going to ignore this and continue to try to get some experience with *wireshark*.
```bash
strings network-dump.flag.pcap
```
#strings

```
...
p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ c e c c a a 7 f }
...
```

```bash
strings network-dump.flag.pcap | grep "p i c o" | tr -d ' ' > flag.txt
```

```
picoCTF{p4ck37_5h4rk_ceccaa7f}
```
#strings #grep #tr 

So after installing *wireshark* I boot it up and...
- File > Open and I open the *pcap* file.
- Analyze > Follow > TCP Stream.
And there in stream 0 is the flag.
#wireshark 

**Flag: *picoCTF{p4ck37_5h4rk_ceccaa7f}***
