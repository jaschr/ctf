#pico2022 #cryptography 

## Challenge:
```md
Can you decrypt this message? Decrypt this [message](https://artifacts.picoctf.net/c/527/cipher.txt) using this key "CYLAB".
```

## Process:
Download the file.
```bash
	wget -q https://artifacts.picoctf.net/c/527/cipher.txt
```
#wget 

View the file.
```bash
cat cipher.txt
```
#cat 

```
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}
```

To solve this I opened up [CyberChef](https://gchq.github.io/CyberChef/) to use it's Vigenère decoder.
![[029_Vigenere.png]]
#cyberchef #vigenere #cipher 

Simple enough.
```bash
echo "picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}" > flag.txt
```
#echo 

**Flag: *picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}***


