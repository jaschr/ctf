#pico2022 #webexploitation 

## Challenge:
```md
Can you get the flag? Go to this [website](http://saturn.picoctf.net:50920/) and see what you can discover.
```

## Process:
Step 1: visit the [website](http://saturn.picoctf.net:50920/).

Step 2: Simply inspect the HTML source. This contained a comment:
```html
<!--picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}-->
```

And there's the flag. So to put it in a *flag.txt* file:
```bash
echo "picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}" > flag.txt
```
#echo 

**Flag: *picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}***
