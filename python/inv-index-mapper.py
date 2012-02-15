#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys, os
import re

def read_input(file):
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9-']*")
    for line in file:
        # split the line into words, ignoring punctuation   
        #yield line.split('_')    
        yield pattern.findall(line)

def getFileName():
	if 'map_input_file' in os.environ:
		return os.environ['map_input_file']
	else:
		return 'none'


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print '%s%s%s' % (word, separator, getFileName())

if __name__ == "__main__":
    main()
