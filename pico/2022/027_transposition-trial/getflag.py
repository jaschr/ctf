#!/usr/bin/env python
with open("message.txt", 'r') as file:
    flag_enc = file.read()
flag = ""
for i in range(2, len(flag_enc), 3):
    flag += flag_enc[i] + flag_enc[i-2] + flag_enc[i-1]
print(flag)
