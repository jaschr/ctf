#pico2022 #forensics

## Challenge:
```md
Download this image file and find the flag.

-   [Download image file](https://artifacts.picoctf.net/c/136/drawing.flag.svg)
```

## Process:
First thing I did was *wget* the file.
```bash
wget -q https://artifacts.picoctf.net/c/136/drawing.flag.svg
```
#wget

Looking through the file I can see the flag after the tspanXXXX elements.

To solve this let's do some shell commands for more fun than just looking at the file.

First, grep all the lines containing *\</tspan>*:
```bash
cat drawing.flag.svg | grep "</tspan>"
```
#cat #grep

This returns all the lines containing *\</tspan>*:
```
 id="tspan3748">p </tspan><tspan
 id="tspan3754">i </tspan><tspan
 id="tspan3756">c </tspan><tspan
 id="tspan3758">o </tspan><tspan
 id="tspan3760">C </tspan><tspan
 id="tspan3762">T </tspan><tspan
 id="tspan3764">F { 3 n h 4 n </tspan><tspan
 id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan></text>
```


Next we add:
```bash
... | cut -d ">" -f 2
```
#cut

Which expands it to this:
```bash
cat drawing.flag.svg | grep "</tspan>" | cut -d ">" -f 2 
```
#cat #grep #cut

Which returns:
```
p </tspan
i </tspan
c </tspan
o </tspan
C </tspan
T </tspan
F { 3 n h 4 n </tspan
c 3 d _ a a b 7 2 9 d d }</tspan
```

This uses *cut* to to cut specific sections of what is passed. The *-d* is the *delimiter* flag. I set the delimiter to a *>* rather than the default *TAB*. The *-f* flag is the *field* flag. This lets me set the field to extract the second field. (*-f 2*)
#cut

Then we cut again by adding:
```bash
... | cut -d "<" -f 1
```
#cut 

Here we are removing anything after part that is the flag.

Expanded is this:
```bash
cat drawing.flag.svg | grep "</tspan>" | cut -d ">" -f 2 | cut -d "<" -f 1
```
#cat #grep #cut

Next we add:
```bash
... | tr -d "\n"
```
#tr

This uses the *tr* command which translates or deletes characters from standard input (stdin) and writes the result to standard output (stdout). The *-d* flag sets it to delete characters in the first set, which is *\\n*, thus deleting all new lines.
#tr

Expanded the command is:
```bash
cat drawing.flag.svg | grep "</tspan>" | cut -d ">" -f 2 | cut -d "<" -f 1 | tr -d "\n"
```
#cat #grep #cut #tr

Which returns:
```
p i c o C T F { 3 n h 4 n c 3 d _ a a b 7 2 9 d d }
```

Next we use *tr* again to remove the spaces.
```bash
... | tr -d " "
```
#tr

Expanded:
```bash
cat drawing.flag.svg | grep "</tspan>" | cut -d ">" -f 2 | cut -d "<" -f 1 | tr -d "\n" | tr -d " "
```
#cat #grep #cut #tr

This results in the flag:
```
picoCTF{3nh4nc3d_aab729dd}
```

To output into a flag.txt file:
```bash
cat drawing.flag.svg | grep "</tspan>" | cut -d ">" -f 2 | cut -d "<" -f 1 | tr -d "\n" | tr -d " " > flag.txt
```
#cat #grep #cut #tr

I also use *echo* to append a newline character to the file. Any further time doing this will not be noted as it's just a personal preference to have the newline character.
```bash
echo "" >> flag.txt
```
#echo

**Flag: *picoCTF{3nh4nc3d_aab729dd}***
