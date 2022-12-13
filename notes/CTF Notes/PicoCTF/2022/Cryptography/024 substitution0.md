#pico2022 #cryptography 

## Challenge:
```md
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message [here](https://artifacts.picoctf.net/c/379/message.txt).
```

## Process:
Using *curl* this time.
```bash
curl https://artifacts.picoctf.net/c/379/message.txt -o message.txt
```
#curl

Taking a look at the file.
```bash
cat message.txt
```
#cat 

Output:
```
EKSZJTCMXOQUDYLFABGPHNRVIW

Mjbjhfly Ujcbeyz eblgj, rxpm e cbenj eyz gpepjui exb, eyz kblhcmp dj pmj kjjpuj
tbld e cuegg segj xy rmxsm xp reg jysulgjz. Xp reg e kjehpxthu gsebekejhg, eyz, ep
pmep pxdj, hyqylry pl yephbeuxgpg—lt slhbgj e cbjep fbxwj xy e gsxjypxtxs flxyp
lt nxjr. Pmjbj rjbj prl blhyz kuesq gflpg yjeb lyj jvpbjdxpi lt pmj kesq, eyz e
ulyc lyj yjeb pmj lpmjb. Pmj gseujg rjbj jvsjjzxycui mebz eyz culggi, rxpm euu pmj
effjebeysj lt khbyxgmjz cluz. Pmj rjxcmp lt pmj xygjsp reg njbi bjdebqekuj, eyz,
peqxyc euu pmxycg xypl slygxzjbepxly, X slhuz mebzui kuedj Ohfxpjb tlb mxg lfxyxly
bjgfjspxyc xp.

Pmj tuec xg: fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}
```

First guess is that the *key* is just a substitution for each letter of the alphabet. So after matching them we get:
```
EKSZJTCMXOQUDYLFABGPHNRVIW
ABCDEFGHIJKLMNOPQRSTUVWXYZ


# This looks like the flag.
fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}
picoCTF{5UB5717U710N_3V0LU710N_59533A2E}
```

And that's the flag.
```bash
echo "picoCTF{5UB5717U710N_3V0LU710N_59533A2E}" > flag.txt
```

**Flag: *picoCTF{5UB5717U710N_3V0LU710N_59533A2E}***
