#pico2022 #cryptography 

## Challenge:
```md
A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. Download the message [here](https://artifacts.picoctf.net/c/414/message.txt).
```

## Process:
Download the given file.
```bash
curl https://artifacts.picoctf.net/c/414/message.txt -o message.txt
```
#curl 

Then viewing the file.
```bash
cat message.txt
```
#cat 

Output:
```
IECj (jqfue cfu ixzelus eqs coxa) xus x emzs fc ifrzlesu jsiludem ifrzsededfy. Ifyesjexyej xus zusjsyesk hdeq x jse fc iqxoosyasj hqdiq esje eqsdu iusxedgdem, esiqydixo (xyk affaodya) jpdooj, xyk zuftosr-jfogdya xtdodem. Iqxoosyasj ljlxoom ifgsu x ylrtsu fc ixesafudsj, xyk hqsy jfogsk, sxiq mdsokj x jeudya (ixoosk x coxa) hqdiq dj jltrdeesk ef xy fyodys jifudya jsugdis. IECj xus x ausxe hxm ef osxuy x hdks xuuxm fc ifrzlesu jsiludem jpdooj dy x jxcs, osaxo sygdufyrsye, xyk xus qfjesk xyk zoxmsk tm rxym jsiludem auflzj xuflyk eqs hfuok cfu cly xyk zuxiedis. Cfu eqdj zuftosr, eqs coxa dj: zdifIEC{CU3NL3YIM_4774IP5_4U3_I001_4871S6CT}
```

Here's the section needed to decrypt.
```
zdifIEC{CU3NL3YIM_4774IP5_4U3_I001_4871S6CT}
```

Here's a [website](https://www.101computing.net/frequency-analysis/) that helps with frequency analysis. The hint for the challenge says to try a *frequency attack*.
![[025_substitution1-1.png]]
#frequencyattack

Taking some assumptions we can assume:
```
eqs coxa dj: zdifIEC{CU3NL3YIM_4774IP5_4U3_I001_4871S6CT}
```
Will become:
```
the flag is: picoCTF{XXXXXXXXX_XXXXXXX_XXX_XXXX_XXXXXXXX}
```

So we know:
```
eqscoxadjzif
theflagispco
```

Which gives us:
![[025_substitution1-2.png]]

From here we can start filling in the blanks.
![[025_substitution1-3.png]]

And the missing substitution left can be assumed to be n->q, giving us the flag:
```bash
echo "picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}" > flag.txt
```
#echo 

**Flag: *picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}***

## Extra:
The full substituion we known:
```
ACDEFGHIJKLMNOPQRSTUXYZ -- with BVW not being used
GFITOVWCSDUYQLKHMEBRANP -- which would be some mix of JXZ 
```

Here's another [website](https://www.guballa.de/substitution-solver) which can use a *frequency attack* to solve this itself. It also is case-sensative, which is much nicer.
![[025_substitution1-4.png]]
![[025_substitution1-5.png]]
#frequencyattack 