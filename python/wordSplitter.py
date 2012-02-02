#!/usr/bin/python
   
import sys
import re

def get_wordcounts(line):
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    for word in  pattern.findall(line):
        print("LongValueSum:" + word.lower() + "\t" + "1")
        

def main(argv):
    line = sys.stdin.readline()
    
    try:
        while line:
            get_wordcounts(line)
            line =  sys.stdin.readline()
    except "end of file":
        return None
     
if __name__ == "__main__":
    main(sys.argv)