#pico2022 #cryptography 

##  Challenge:
```md
A new modular challenge! Download the message [here](https://artifacts.picoctf.net/c/499/message.txt). Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
```

## Process:
First step was to *wget* the file.
```bash
wget -q https://artifacts.picoctf.net/c/499/message.txt
```
#wget

Next was to copy the *mod1.py* from [[002 basic-mod1]] to the new folder.
```bash
cp ../002_basic-mod1/mod1.py mod2.py
```
#cp

After this I edited the *mod2.py* file to work with the new modulo.
```python
#!/usr/bin/env python

charset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o
flag = "picoCTF{"
msg_file = "message.txt"

with open(msg_file, 'r', encoding='utf-8') as file:
  for line in file:
    numbers = line.split()
      for number in numbers:
        module = int(number) % 41
        for i in range(41):
	      if (module * i) % 41 == 1:
		    flag += charset[i - 1]
		    break
		    
print(flag + "}")
```
#python 

The original script would account for the list index that is out of range.

Then I ran...
```bash
python mod2.py > flag.txt
```
#python 

Which outputted the flag to the flag.txt file.

**Flag: *picoCTF{1nv3r53ly_h4rd_c680bdc1}***


