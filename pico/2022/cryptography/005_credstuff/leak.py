#!/usr/bin/env python

import codecs

user = "cultiris"
user_index = 1

with open("leak/usernames.txt", 'r') as users:
    for line in users:
        if line.strip() == user:
            break
        user_index += 1

with open("leak/passwords.txt", 'r') as passwords:
    all_lines = passwords.readlines()
    pass_index = user_index - 1

    flag_encrypted = all_lines[pass_index]

    flag = codecs.decode(flag_encrypted, 'rot_13')

    print(flag)
