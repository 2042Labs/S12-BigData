#!/usr/bin/env python
# encoding: utf-8
"""
markov.py

Created by Maksim Tsvetovat on 2012-02-02.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from collections import defaultdict
import random

f='../output/part-00000'

f_in=open(f,'rb')

bigram_index=defaultdict(list)

for line in f_in:
    row=line.strip().split('\t')
    if len(row) == 2:
        if int(row[1]) > 1:
            word1, word2 = row[0].split('_')
            bigram_index[word1].append(word2)


### next step :: instead of randomly choosing a word, choose one based on frequency of usage
### i.e. the goal is to write a nonsense-generator that sounds like Shakespeare.            
word="the"
while True:
    print word,
    next=bigram_index[word]
    try : 
        word = next[int(random.uniform(0,len(next)))]
    except : 
        break
        