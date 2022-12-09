#pico2022 #webexploitation 

## Challenge:
```md
The flag is somewhere on this web application not necessarily on the website. Find it. Check [this](http://saturn.picoctf.net:65352/) out.
```

## Process:
Peeking through the [website](https://saturn.picoctf.net:65352/) I look at the [*robots.txt*](http://saturn.picoctf.net:65352/robots.txt)
```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

The double equals makes me think it is base64. Let's write some *python*.
```python
#!/usr/bin/env python3

import base64

b64 = "anMvbXlmaWxlLnR4dA=="

decoded = base64.b64decode(b64)
print(decoded.decode('utf-8'))
```
#python 

This outputs:
```
js/myfile.txt
```

Opening up the website to the [file](http://saturn.picoctf.net:65352/js/myfile.txt).
![[035_Roboto_Sans.png]]

Save the flag.
```bash
echo "picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}" > flag.txt
```
#echo 

**Flag: *picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}***
