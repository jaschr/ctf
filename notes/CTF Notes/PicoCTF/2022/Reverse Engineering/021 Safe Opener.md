#pico2022 #reverseengineering 

## Challenge:
```md
Can you open this safe? I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: `picoCTF{password}`
```

## Process:
I first *wget* the file.
```bash
wget -q https://artifacts.picoctf.net/c/463/SafeOpener.java
```
#wget 

I take a look at the *java* file. There I see the encoder is *base64* and the encoded key is given in plaintext.
```java
...
 Base64.Encoder encoder = Base64.getEncoder();
...
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
...
```
#java #base64

To decode the *base64* I wrote a small *python* script.
```python
#!/usr/bin/env python
import base64
encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"
decodedkey = base64.b64decode(encodedkey)
print("picoCTF{" + decodedkey.decode('utf-8') + "}")
```
#python 

And this gave me the flag in the correct format.
```bash
python base64decode.py > flag.txt
```
#python 

**Flag: *picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}***
