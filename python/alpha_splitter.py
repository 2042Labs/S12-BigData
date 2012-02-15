#!/usr/bin/env python
# encoding: utf-8
"""
alpha_splitter.py

Created by Maksim Tsvetovat on 2012-02-09.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os


f=open("wikipedia_titles.txt",'rb')
letter="Z"
for line in f:
    if line.startswith(letter):
        outfile.write(line)
    else:
        letter=line[:1] ## filename will be the first letter of the line
        if letter=='/':
            outfile=open("split_slash.txt",'wb')
        elif letter=='.':
            outfile=open("split_dot.txt",'wb')
        else:
            outfile=open("split_"+letter+".txt",'wb')
        outfile.write(line)
            