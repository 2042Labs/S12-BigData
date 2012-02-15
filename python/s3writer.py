#!/usr/bin/env python
# encoding: utf-8
"""
s3writer.py

Created by Maksim Tsvetovat on 2011-12-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import datetime

class s3writer(object):
    """stores json files in an S3 bucket for the website to pick up"""
    
    def __init__(self):
        aws_access_key='AKIAIC65JLYAEJA7IRBA'
        aws_secret_key='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'
    
        
        self.acl="public-read"
        self.base_url='data.electiongauge.com'
        self.conn = S3Connection(aws_access_key, aws_secret_key)
        self.public_bucket= self.conn.create_bucket('css739bigdata')
        self.dir={}
        
    def write(self,name,content):
        """Store *content* in a location designated by *key* in a public bucket (default) or private bucket (if private=True)"""
        bucket=self.public_bucket
            
        nm=name.split('.')[0]
#        js_content="var "+nm+" = " + content + ";"
        
        k = Key(bucket)
        k.key=name
        k.set_contents_from_string(content,headers={'Content-Type': 'text/plain', 'Access-Control-Allow-Origin': '*'})
        k.set_acl(self.acl)
#        if not private:
#            self.dir[name]=str(datetime.datetime.now())
        
    def read(self,key):
        """get content from a location designated by *key* in a public bucket (default) or private bucket (if private=True)"""
        bucket=self.public_bucket

        k = Key(bucket)
        k.key=key
        return(k.get_contents_as_string())
        
    def update_public_index(self):
        html_head="<html><body>\n"
        html_foot="</body></html>\n"
        
        html=html_head
        for k,v in self.dir.iteritems():
            html+='<a href=\"'+k+'\">'+k+"</a>:"+v+"\n"
        
        html+=html_foot
        self.write("index.html",html)