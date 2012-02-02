from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto

AWS_KEY='AKIAIQ7VG4UORIN75ZSA'
AWS_SECRET='jzxajGx8gzwX+ymYXJ0/5heCjkPtWLQkICYRn7Vj'

conn = EmrConnection(AWS_KEY, AWS_SECRET)

step = StreamingStep(name='My wordcount example',
                      mapper='s3n://css739/wordcount/bigramSplitter.py',
                      reducer='aggregate',
                      input='s3n://smalldata/wikipedia_titles.txt',
                      output='s3n://css739/wordcount/bigram_count_output')
                      
                      
jobid = conn.run_jobflow(name='My jobflow', log_uri='s3n://css739/wordcount/jobflow_logs',steps=[step])

conn.describe_jobflow(jobid).state
