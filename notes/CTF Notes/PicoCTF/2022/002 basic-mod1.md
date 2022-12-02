#pico2022 #cryptography 

## Challenge:
```md
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/393/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
```

## Process:
First step was to wget the message.txt.
```bash
wget -q https://artifacts.picoctf.net/c/393/message.txt
```
#wget

The challenge states:
	Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

So to do this I created a python script.
```python
#!/usr/bin/env python

charset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o
flag = "picoCTF{"
msg_file = "message.txt"

with open(msg_file, 'r', encoding='utf-8') as file:
  for line in file:
    numbers = line.split()
      for number in numbers:
        flag = flag + (charset[int(number)%37])
print(flag + "}")
```
#python 

Then I ran...
```bash
python mod1.py > flag.txt
```
#python 

Which outputted the flag to the flag.txt file.

**Flag: *picoCTF{r0und_n_r0und_79c18fb3}***