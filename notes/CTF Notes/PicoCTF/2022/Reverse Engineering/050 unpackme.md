#pico2022 #reverseengineering 

## Challenge:
```md
Can you get the flag? Reverse engineer this [binary](https://artifacts.picoctf.net/c/365/unpackme-upx).
```

## Process:
Download the binary.
```bash
curl -O https://artifacts.picoctf.net/c/365/unpackme-upx
```
#curl 

The binary was packed with ```upx```. We use it to unpack the file.
```bash
upx -d unpackme-upx
```
#upx

Then opening the unpacked file in *ghidra*.
![[050_unpackme.png]]
#ghidra 

Now let's convert that to decimal.
```python
#!/usr/bin/env python3

h = "0xb83cb"

d = int(h, base=16)

print(d)
```
#python 

```
754635
```

Make the binary executable.
```bash
chmod +x unpackme-upx
```
#chmod 

Pipe the python output to the binary.
```bash
python conv.py | ./unpackme-upx
```
#python 

```
What's my favorite number? picoCTF{up><_m3_f7w_77ad107e}
```

Found the flag.
```bash
echo "picoCTF{up><_m3_f7w_77ad107e}" > flag.txt
```
#echo 

**Flag: *picoCTF{up><_m3_f7w_77ad107e}***
