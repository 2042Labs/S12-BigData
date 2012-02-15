import sys
import os
from collections import defaultdict
import random

f='../output/part-00000'

f_in=open(f,'rb')

nums=[]

for line in f_in:
    row=line.strip().split('\t')
    if len(row) == 2:
        nums.append(int(row[1]))