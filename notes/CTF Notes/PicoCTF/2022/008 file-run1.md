#pico2022 #reverseengineering

## Challenge:
```md
A program has been provided to you, what happens if you try to run it on the command line? Download the program [here](https://artifacts.picoctf.net/c/308/run).
```

## Process:
Step 1: *wget*
```bash
wget -q https://artifacts.picoctf.net/c/308/run
```
#wget 

Step 2: *chmod*
```bash
chmod +x run
```
#chmod 

Step 3: Run the program
```bash
./run
```

Result:
```
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}
```

Then we can use *sed* to strip out and return only the flag:
```bash
./run | sed 's/.*: //'
```
#sed

*SED* means *stream editor*. The *s/* specifies that it will be a substitution. This subsitues all things matching *\*:*   and replaces it with nothing.
#sed #streameditor

Then to get the flag.txt:
```bash
./run | sed 's/.*: //' > flag.txt
```
#sed

**Flag: *picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}***


