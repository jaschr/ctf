#!/usr/bin/env python

with open("flag", 'r') as file:
    flag_file = file.read()
    flag = b''.fromhex(flag_file).decode("utf-8").strip()
print(flag)
