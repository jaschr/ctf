#pico2022 #cryptography 

## Challenge:
```md
Smash the stack Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/520/vuln). You can view source [here](https://artifacts.picoctf.net/c/520/vuln.c). And connect with it using: `nc saturn.picoctf.net 53935`
```

## Process:
First step: *wget*
```bash
wget -q https://artifacts.picoctf.net/c/534/leak.tar
```
#wget 

Then *untar* the file:
```bash
tar -xf leak.tar
```
#tar

This gives me a directory *leak* which contains two files:
- usernames.txt
- passwords.txt

The index of the username aligns with the index of the password.

I could have looked up what line the username was on and then do the same in the password file, but that didn't seem as fun.

So I wrote a python script.

```python
#!/usr/bin/env python

user = "cultiris"
user_index = 1

with open("leak/usernames.txt", 'r') as users:
    for line in users:
        if line.strip() == user:
            break
        user_index += 1

with open("leak/passwords.txt", 'r') as passwords:
    all_lines = passwords.readlines()
    pass_index = user_index - 1

    flag = all_lines[pass_index]

    print(flag)
```
#python 

Which gives me: *cvpbPGS{P7e1S_54I35_71Z3}*

So seeing this I tried a *ROT-13* cipher on it to see if it would give me the decrypted flag. I changed up the python script slightly.
```python
    flag_encrypted = all_lines[pass_index]

    flag = codecs.decode(flag_encrypted, 'rot_13')

    print(flag)
```
#python 

Running this gave me the flag. So next is to output this to a flag.txt file.
```bash
python leak.py > flag.txt
```
#python 

**Flag: *picoCTF{C7r1F_54V35_71M3}***