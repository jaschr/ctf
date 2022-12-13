#pico2022 #webexploitation 

## Challenge:
```md
Can you get the flag? Go to this [website](http://saturn.picoctf.net:55287/) and see what you can discover.
```

## Process:
Open up the [website](http://saturn.picoctf.net:55287/) and open up the inspector. I clicked the continue as guest button and checked the cookies.
![[034_Power_Cookie-0.png]]

And I changed the cooke value.
![[034_Power_Cookie-1.png]]

And this gives me the cookie.
```bash
echo "picoCTF{gr4d3_A_c00k13_5d2505be}" > flag.txt
```
#echo 

**Flag: *picoCTF{gr4d3_A_c00k13_5d2505be}***
