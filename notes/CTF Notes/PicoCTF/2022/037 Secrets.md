#pico2022 #webexploitation 

## Challenge:
```md
We have several pages hidden. Can you find the one with the flag? The website is running [here](http://saturn.picoctf.net:61481/).
```

## Process:
Open up the [website](http://saturn.picoctf.net:61481/) and check out the inspector. Here I see a folder *secret/* so I visit the [secret page](http://saturn.picoctf.net:61481/secret/). 

From here within the *head* I see another folder: *hidden/*. So I visit [secret/hidden/](http://saturn.picoctf.net:61481/secret/hidden/).

From here I see another folder:  [superhidden](http://saturn.picoctf.net:61481/secret/hidden/superhidden/).

And viewing the source gives us the flag.
![[037_Secrets.png]]

```bash
echo "picoCTF{succ3ss_@h3n1c@10n_39849bcf}" > flag.txt
```
#echo 

**Flag: *picoCTF{succ3ss_@h3n1c@10n_39849bcf}***
