#pico2022 #forensics 

## Challenge:
```md
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data [here](https://artifacts.picoctf.net/c/294/anthem.flag.txt).
```

## Process:
First is to *wget* the file.
```bash
wget -q https://artifacts.picoctf.net/c/294/anthem.flag.txt
```
#wget 

I opened up *vim* and looked at the file.
```bash
nvim anthem.flag.txt
```
#neovim #vim #nvim

Then I searched the file to match the start of the flag.
```vim
:%s/pico
```

Which gave me the flag. I *echoed* this into a flag file.
```bash
echo "picoCTF{gr3p_15_@w3s0m3_4c479940}" > flag.txt
```
#echo 

**Flag: *picoCTF{gr3p_15_@w3s0m3_4c479940}***