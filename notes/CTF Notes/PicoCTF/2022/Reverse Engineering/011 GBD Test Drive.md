#pico2022  #reverseengineering 

## Challenge:
```md
Can you get the flag? Download this [binary](https://artifacts.picoctf.net/c/115/gdbme). Here's the test drive instructions:

-   `$ chmod +x gdbme`
-   `$ gdb gdbme`
-   `(gdb) layout asm`
-   `(gdb) break *(main+99)`
-   `(gdb) run`
-   `(gdb) jump *(main+104)`
```

## Process:
Step 1: *wget* the file.
```bash
wget -q https://artifacts.picoctf.net/c/115/gdbme
```
#wget 

Step 2: Follow the instructions in the challenge.
```bash
chmod +x gbdme
```
#chmod 

```bash
sudo apt install gdb
```
#sudo #apt #gdb


Here's the commands then entered:
```bash
gdb gdbme

layout asm
break \*(main+99)
run
jump \*(main+104)
```
#gdb 

This gave me the flag.

**Flag: *picoCTF{d3bugg3r_dr1v3_197c378a}***

## Extra:
*GDB* is the *GNU Project Debugger*. GDB offers extensive facilities for tracing and altering the execution of computer programs. The user can monitor and modify the values of programs' internal variables, and even call functions independently of the program's normal behavior. [Source.](https://en.wikipedia.org/wiki/GNU_Debugger)
