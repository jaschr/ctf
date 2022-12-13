#pico2022 #reverseengineering 

## Challenge:
```md
Can you get the flag? Reverse engineer this [binary](https://artifacts.picoctf.net/c/301/bbbbloat).
```

## Process:
Download the binary.
```bash
curl -O https://artifacts.picoctf.net/c/301/bbbbloat
```
#curl 

Then I made the binary executable.
```bash
chmod +x bbbbloat
```
#chmod 

Then I opened the binary in *ghidra*. And looked for where it checks for the correct number.
![[041_Bbbbloat.png]]
#ghidra 

Here I converted the hexadecimal to decimal.
```
0x86187
```

```python
#!/usr/bin/env python3

h = '0x86187'

d = int(h, base=16)

print(d)
```
#python 

This outputs:
```
549255
```

So we try it.
```bash
python hextodec.py | ./bbbbloat
```
#python 

Which outputs:
```
What's my favorite number? picoCTF{cu7_7h3_bl047_36dd316a}
```

Save the flag.
```bash
echo "picoCTF{cu7_7h3_bl047_36dd316a}" > flag.txt
```
#echo 

**Flag: *picoCTF{cu7_7h3_bl047_36dd316a}***
