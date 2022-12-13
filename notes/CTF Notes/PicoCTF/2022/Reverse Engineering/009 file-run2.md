#pico2022 #reverseengineering

## Challenge:
```md
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program [here](https://artifacts.picoctf.net/c/351/run).
```

## Process:
Start with ```wget``` and ```chmod```.
```bash
wget -q https://artifacts.picoctf.net/c/351/run
chmod +x run
```
#wget #chmod 

Running this program and passing *Hello!*:
```bash
./run Hello!
```

Results with:
```
The flag is: picoCTF{F1r57_4rgum3n7_be0714da}
```

Then doing the same steps in [[008 file-run1]] we can strip out just the flag and output it to a flag.txt file.
```bash
./run Hello! | sed 's/.*: //' > flag.txt
```
#sed

**Flag: *picoCTF{F1r57_4rgum3n7_be0714da}*

