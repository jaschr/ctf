#pico2022 #cryptography 

## Challenge:
```md
It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher? Download the message [here](https://artifacts.picoctf.net/c/107/message.txt).
```

## Process:
First I *curl* the file.
```bash
curl https://artifacts.picoctf.net/c/107/message.txt -o message.txt
```
#curl 

Using the same [website](https://www.guballa.de/substitution-solver) as in [[025 substitution1]].
![[026_substitution2.png]]
#frequencyattack 

The *frequency attack* worked!
```bash
echo "picoCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}" > flag.txt
```
#echo 

**Flag: *picoCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}***
