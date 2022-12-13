#pico2022 #reverseengineering 

## Challenge:
```md
Can you get the flag? Run this [Python program](https://artifacts.picoctf.net/c/386/patchme.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/386/flag.txt.enc).
```

## Process:
```wget``` both files.
```bash
wget -q https://artifacts.picoctf.net/c/386/patchme.flag.py
wget -q https://artifacts.picoctf.net/c/386/flag.txt.enc
```
#wget 

Opening the *python* file I see:
```python
if( user_pw == "ak98" + \
  "-=90" + \
  "adfjhgj321" + \
  "sleuth9000"):
print("Welcome back... your flag, user:")
decryption = str_xor(flag_enc.decode(), "utilitarian")
print(decryption)
```
#python 

So I change it to in *password.py*:
```python
print("ak98" + \
 "-=90" + \
 "adfjhgj321" + \
 "sleuth9000")
```
#python

```
ak98-=90adfjhgj321sleuth9000
```

And so I use this as the password after running the given *python* file.
```bash
python patchme.flag.py
```
#python 

```
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
```

Which outputs the flag. ```echo``` it.
```bash
echo "picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}" > flag.txt
```
#echo 

**Flag: *picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}***

## Extra:
Another easy way to do this is to edit the hardcoded password.
```python
if( user_pw == "password"):
print(decryption)
```
#python 

And now re-running the program and entering *password* for the password gives us the flag.
```bash
python patchme.flag.py
```
#python 

```
Please enter correct password for flag: password
```

```
picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
```