from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto

AWS_KEY='AKIAIQ7VG4UORIN75ZSA'
AWS_SECRET='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'

conn = EmrConnection(AWS_KEY, AWS_SECRET)

filelist="""split_!.txt
split_".txt
split_$.txt
split_%.txt
split_&.txt
split_'.txt
split_(.txt
split_).txt
split_*.txt
split_+.txt
split_,.txt
split_-.txt
split_0.txt
split_1.txt
split_2.txt
split_3.txt
split_4.txt
split_5.txt
split_6.txt
split_7.txt
split_8.txt
split_9.txt
split_;.txt
split_=.txt
split_?.txt
split_@.txt
split_A.txt
split_B.txt
split_C.txt
split_D.txt
split_E.txt
split_F.txt
split_G.txt
split_H.txt
split_I.txt
split_J.txt
split_K.txt
split_L.txt
split_M.txt
split_N.txt
split_O.txt
split_Q.txt
split_R.txt
split_S.txt
split_T.txt
split_U.txt
split_V.txt
split_W.txt
split_X.txt
split_Y.txt
split_Z.txt
split_\.txt
split_^.txt
split_`.txt
split_dot.txt
split_p.txt
split_slash.txt
split_~.txt""".split('\n')

files_short="""split_A.txt
split_B.txt
split_C.txt
split_D.txt
split_E.txt
split_F.txt
split_G.txt
split_H.txt
split_I.txt
split_J.txt
split_K.txt
split_L.txt
split_M.txt""".split('\n')

input_files=['s3n://smalldata/'+f for f in files_short]


step = StreamingStep(name='Inverted Index ',
                      mapper='s3n://css739/invIndex/inv-index-mapper.py',
                      reducer='s3n://css739/invIndex/inv-index-mapper.py',
                      input=input_files,
                      #input='s3n://smalldata/wikipedia_titles.txt',
                      output='s3n://css739/invIndex/invindex_output2')
                      #cache_files=['s3n://css739/invindex/english_stoplist.py'])
                      
                      
jobid = conn.run_jobflow(name='Inverted Index', log_uri='s3n://css739/invIndex/jobflow_logs',steps=[step])

conn.describe_jobflow(jobid).state
