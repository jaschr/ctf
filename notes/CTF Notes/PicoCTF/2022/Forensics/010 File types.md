#pico2022  #forensics 

## Challenge:
```md
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from [here](https://artifacts.picoctf.net/c/323/Flag.pdf).
```

## Process:
Step 1: *wget*
```bash
wget -q https://artifacts.picoctf.net/c/323/Flag.pdf
```
#wget 

Then I opened up the file in *neovim* (*vim*) and noticed it was a shell script. I then changed the file to a *.sh* file.
```bash
mv Flag.pdf flag.sh
```
#mv

Then give executable permissions:
```bash
chmod +x flag.sh
```
#chmod 

Then run the shell script:
```bash
./flag.sh
```

This told me I was missing uudecode. So after a quick google I installed (re-installed) *sharutils*.
```bash
sudo apt install sharutils
```
#sudo #apt #sharutils #uudecode

Then I re-ran the file and it outputted a new file *flag*.
```bash
cat flag
```
#cat 

Which outputs:
```
!<arch>
flag/           0           0     0     644     1024      `
i�h� ѣ##'SGzѨrш@4�hb0C@1F�kϹ=�@{O}ѦM4�
�<M�hVτHI�W�8"'f0�!�xr_fT h�ª~�ѣM�@4h#G�@�@S&

�'ÅO{o�K51]<�T��s-�Υ�A2�͛$:e�/9�>�pKb&q['
Z3�#Ŏ.�!,�        EX?AX%-�Ó.x�G.�i�+vCBx�I�!�ۮn")���$>#By
          TRAILER!!!
```

The *!\<arch>* indicates a *.ar archive* (Google told me this). So I changed the flag to have a *.ar* extention.
```bash
mv flag flag.ar
```
#mv 

Then using *ar* to extract the file:
```bash
ar -x flag.ar
```
#ar 

Outputs a new *flag* file.
```bash
cat flag
```
#cat 

```
i�h� ѣ##'SGzѨrш@4�hb0C@1F�kϹ=�@{O}ѦM4�
�<M�hVτHI�W�8"'f0�!�xr_fT h�ª~�ѣM�@4h#G�@�@S&

�'ÅO{o�K51]<�T��s-�Υ�A2�͛$:e�/9�>�pKb&q['
Z3�#Ŏ.�!,�        EX?AX%-�Ó.x�G.�i�+vCBx�I�!�ۮn")���$>#By
          TRAILER!!!
```

Then I ran:
```bash
file flag
```
#file

This tells me:
```
flag: cpio archive
```

So...
```bash
mv flag flag.cpio
```
#mv 

And run *cpio* with the flags *-i* and *-d*. *-i* is for *extract* and *-d* will *create leading directories where necessary*.
```bash
cpio -id < flag.cpio
```
#cpio

New *flag* file.
```bash
cat flag
```
#cat 

```
i�h� ѣ##'SGzѨrш@4�hb0C@1F}ѦM4�
�<M�hVτHI�W�8"'f0�!�xr_fT h�ª~�ѣM�@4h#G�@�@S&

�'ÅO{o�K51]<�T��s-�Υ�A2�͛$:e�/9�>�pKb&q['
Z3�#Ŏ.�!,
```

Run *file*
```bash
file flag
```
#file 

```
flag: bzip2 compressed data, block size = 900k
```

Change extention
```bash
mv flag flag.bz2
```
#mv

And extract with *bzip2*. The *-d* flag means *decompress*.
```bash
bzip2 -d flag.bz2
```
#bzip2 #bz2

Another *flag* file.
```bash
cat flag
```
#cat

```
<70bflagILZIP
             	O�6�o��X��1kEy;"�i�(;Y�&�9%
NjNy5i({j�©D��Q/�U��w8�>4Ԥit3h.m%�(��vFi|BMW�iSnqy[]gp?c'�}z{$�c^�I3�jI
```

Try *file* again...
```bash
file flag
```
#file 

```
flag: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
```

Repeat.
```bash
mv flag flag.gz
```
#mv 

Now with *gzip*.
```bash
gzip -d flag.gz
```
#gz #gzip

Another.
```bash
cat flag
```
#cat 

```
LZIP
    	O�6�o��X��1kEy;"�i�(;Y�&�9%
NjNy5i({j�©D��Q/�U��w8�>4Ԥit3h.m%�(��vFi|BMW�iSnqy[]gp?c'�}z{$�c^�I
```

Run *file*
```bash
file flag
```
#file 

```
flag: lzip compressed data, version: 1
```

Change extension again
```bash
mv flag flag.lzip
```
#mv 

And run *lzip*. (And install *lzip*)
```bash
sudo apt install lzip
```
#sudo #apt #lzip 

```bash
lzip -d flag.lzip
```
#lzip

A new file: *flag.lzip.out*
```bash
cat flag.lzip.out
```
#cat 

```
"Mds]�DDxʶ�kw%e8�g��Lɹ�YFʘ咗3
81J{���ϠL T�H�<v\^��4�*�Lcd��<Z��מÕ�r#	�9yy*݆%fC��X��
                                                     otCaw9Y!�5?0f��M~5�\*S
,)!	*��~ζ"'�/.�$�E�~UY�]+̙
```

Run *file*
```bash
file flag.lzip.out
```
#file 

```
flag.lzip.out: LZ4 compressed data (v1.4+)
```

Repeat.
```bash
mv flag.lzip.out flag.lz4
```
#mv 

Install *lz4*...
```bash
sudo apt install lz4
```
#sudo #apt #lz4 

Run *lz4*
```bash
lz4 -d flag.lz4
```
#lz4 

Now keep repeating the process...
```bash
cat flag
```
#cat 

```
]DDxʶ�kw%e8�g��Lɹ�YFʘ咗3
81J{���ϠL T�H�<v\^��4�*�Lcd��<Z��מÕ�r#	�9yy*݆%fC��X��
                                                     otCaw9Y!�5?0f��M~5�\*S
,)!	*��~ζ"'�/.�$�E�~UY�]
```

```bash
file flag
```
#file 

```
flag: LZMA compressed data, non-streamed, size 255
```

```bash
mv flag flag.lzma
```
#mv 

```bash
lzma -d flag.lzma
```
#lzma

```bash
cat flag
```
#cat 

```
LZO

@ 	@b07<flagD�,�ŉg[LZIP
                            ~����G_�
                                    ��uR�_�d`�/��=�+
                                                    M8ؠ(&$��L�|f���Ѳ�k��
<95.g�#���XՇM1^~ǈ                                                       �q`tٻ"���p�8�!
                 %̜�
```

```bash
file flag
```
#file 

```
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix
```

```bash
mv flag flag.lzop
```
#mv

```bash
sudo apt install lzop
```
#sudo #apt #lzop

```bash
lzop -d flag.lzop
```
#lzop 

```bash
cat flag
```
#cat 

```
LZIP
    ~����G_�
            ��uR�_�d`�/��=�+
                            M8ؠ(&$��L�|f���Ѳ�k��
<95.g�#���XՇM1^~ǈ                               �q`tٻ"���p�8�!
                 %̜�
```

```bash
file flag
```
#file 

```
flag: lzip compressed data, version: 1
```

```bash
mv flag flag.lzip
```
#mv 

```bash
lzip -d flag.lzip
```
#lzip 

```bash
cat flag.lzip.out
```
#cat 

```
7zXZ�F!t/�m]]
3�Օ$;3Xe�<��Uq�M�D��vZ/=f!2�L:}m0Gyn�qt�YZ
```

```bash
file flag.lzip.out
```
#file

```
flag.lzip.out: XZ compressed data, checksum CRC64
```

```bash
mv flag.lzip.out flag.xz
```
#mv 

```bash
xz -d flag.xz
```
#xz

```bash
cat flag
```
#cat 

```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
```

```bash
file flag
```
#file 

```
flag: ASCII text
```

FINALLY!
```bash
cat flag
```
#cat 

```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
```

From here I converted the *HEX* to *ASCII Characters* using *python*:
```python
#!/usr/bin/env python

  with open("flag", 'r') as file:
    flag_file = file.read()
    flag = b''.fromhex(flag_file).decode("utf-8").strip()
print(flag)
```
#python

And running this:
```bash
python flag.py
```
#python 

```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
```

After all that, finally a flag.
```
python flag.py > flag.txt
```
#python 

**Flag: *picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}***
