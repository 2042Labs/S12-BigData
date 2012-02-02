#!/usr/bin/env python
# encoding: utf-8
"""
dynamo_test.py

Created by Maksim Tsvetovat on 2012-02-02.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto

AWS_KEY='AKIAIQ7VG4UORIN75ZSA'
AWS_SECRET='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'

conn = boto.connect_dynamodb(
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET)
        
conn.list_tables()