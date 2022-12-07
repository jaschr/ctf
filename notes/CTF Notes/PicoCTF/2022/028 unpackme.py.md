#pico2022 #reverseengineering 

## Challenge:
```md
Can you get the flag? Reverse engineer this [Python program](https://artifacts.picoctf.net/c/464/unpackme.flag.py).
```

## Process:
Download the file.
```bash
curl -O https://artifacts.picoctf.net/c/464/unpackme.flag.py
```

Open the *python* script in *vim*.
```python
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABiMD04m0Z6CohVV7ozdwHqtgc2__CuAFGG8rWhZBTL0lhfzp-mhu9LYNMnMQMGO-7tEwy3DJ2Y8yjogvzyojFETwN9YEIPXTnO9F1QnkPypWTgjISGve4gcSerJMs694oKcIdKHuVaSxOg1MMNs5k9iPaBIPU7xOKQqCyhnf_f4yUvLdMcer38BqRptocJNvKlyWN8h7ikoWL0zlssxd8OJyPujMz78HZaefvUouvq6LDtPVqRBJFPgSJYf1nHpHKFa1O0zJ6UpTe6ba3PPAxCVXutNg=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```
#python 

I simply print out the *plain.decode()*.
```python
...
plain = f.decrypt(payload)
print(plain.decode())
exec(plain.decode())
```
#python 

This outputs:
```
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_5274ff21}')
else:
  print('That password is incorrect.')
What's the password?
```

Then from here:
```
What's the password? batteryhorse
```

And the flag has been given.
```bash
echo "picoCTF{175_chr157m45_5274ff21}" > flag.txt
```
#echo 

**Flag: *picoCTF{175_chr157m45_5274ff21}***
