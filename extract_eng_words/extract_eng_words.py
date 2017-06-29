#!/usr/bin/env python
#-*-coding:utf-8-*-

import re

with open("from.txt") as f:
    lines = f.readlines()
    lst=[]
    pattern = re.compile(r'\b[A-z]+\b')
    for line in lines:
        lst += re.findall(pattern, line)
    lst.sort()
    to = "\n".join(lst)
    with open("to.txt", "w") as t:
        t.write(to)