#!/usr/bin/env python

charset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","_"]
flag = "picoCTF{"
msg_file = "message.txt"

with open(msg_file, 'r', encoding='utf-8') as file:
    for line in file:
        numbers = line.split()
        for number in numbers:
            flag = flag + (charset[int(number)%37])
print(flag + "}")
