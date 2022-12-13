#pico2022 #cryptography 

## Challenge:
```md
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message [here](https://artifacts.picoctf.net/c/456/message.txt).
```

## Process:
Using *curl* again.
```bash
curl -O https://artifacts.picoctf.net/c/456/message.txt
```
#curl 

View the file:
```bash
cat message.txt
```
#cat 

Output:
```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4
```

I look at this cipher text and see a pattern. Every group of 3 letters has the first letter in the 3rd position. I am going to use a *python* script to fix this.
```python
#!/usr/bin/env python
with open("message.txt", 'r') as file:
    flag_enc = file.read()
flag = ""
for i in range(2, len(flag_enc), 3):
    flag += flag_enc[i] + flag_enc[i-2] + flag_enc[i-1]
print(flag)
```
#python 

Result:
```
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
```

Decrypted!
```bash
echo "picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}" > flag.txt
```
#echo 

**Flag: *picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}***
