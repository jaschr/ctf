#!/usr/bin/env python

import re

flag = ""

with open("drawing.flag.svg", 'r') as file:
    file_string = file.read()
    regex = re.search('^.*tspan.*">(.*)', file_string)

    print(regex.groups())
print(flag)
