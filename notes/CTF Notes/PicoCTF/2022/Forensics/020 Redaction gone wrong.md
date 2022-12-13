#pico2022 #forensics 

## Challenge:
```md
Now you DON’T see me. This [report](https://artifacts.picoctf.net/c/264/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
```

## Process:
First: *wget*.
```bash
wget -q https://artifacts.picoctf.net/c/264/Financial_Report_for_ABC_Labs.pdf
```
#wget 

I used *firefox* to open the *pdf*. The redacted text was still beneath the black boxes. I was able to copy the content beneath.
```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.  
Breakdown - Just painted over in MS word.  
Cost Benefit Analysis  
Credit Debit  
This is not the flag, keep looking  
Expenses from the  
picoCTF{C4n_Y0u_S33_m3_fully}  
Redacted document.
```
#firefox #pdf

And would you look at that.
```bash
echo "picoCTF{C4n_Y0u_S33_m3_fully}" > flag.txt
```
#echo 

**Flag: picoCTF{C4n_Y0u_S33_m3_fully}***
