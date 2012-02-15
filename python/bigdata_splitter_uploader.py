#!/usr/bin/env python
# encoding: utf-8
"""
bigdata_splitter_uploader.py

Created by Maksim Tsvetovat on 2012-02-09.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto
import s3writer
import xmllib


s3=s3writer.s3writer()

def read_page(infile):
    text="<page>\n"
    for line in infile:
        if line.strip().startswith("<title>"):
            title=line.replace("<title>","").replace("</title>","").strip()
        if line.strip() == "<page>": 
            return title, text
        text+=line


infile=open("../bigdata/Wikipedia2012/Wikipedia.Articles.2012.xml",'rb')

##skip until the start of the first article
for line in infile:
    if line.strip() == "<page>": break

print read_page(infile)