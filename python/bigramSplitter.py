#!/usr/bin/python
   
import sys
import re
from english_stoplist import stoplist

def get_bigrams(line):
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    prev_word=""
    for word in  pattern.findall(line):
        word=word.lower()
        if word in stoplist: continue
        if prev_word!="":
            print("LongValueSum:" + prev_word+"_"+word + "\t" + "1")
        prev_word=word
        

def main(argv):
    line = sys.stdin.readline()
    
    try:
        while line:
            get_bigrams(line)
            line =  sys.stdin.readline()
    except "end of file":
        return None
     
if __name__ == "__main__":
    main(sys.argv)