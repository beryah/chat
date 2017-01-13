import requests
import zipfile
import os
import time
import sys
from StringIO import StringIO

sessionId = 301
token = "197691"
seq = 1
#s3_url = 'https://airsupportplusdev-jp.s3-ap-northeast-1.amazonaws.com/302-485346?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJE3UT3C7KVNMOJUQ%2F20170113%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Date=20170113T032922Z&X-Amz-Expires=86400&X-Amz-Signature=a2d668ac210519046b275b478a71ce7112215046ceaa5789fe38d39c1545e22a&X-Amz-SignedHeaders=host'
s3_url = 'https://airsupportplusdev-jp.s3-ap-northeast-1.amazonaws.com/301-197691?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJE3UT3C7KVNMOJUQ%2F20170113%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Date=20170113T025517Z&X-Amz-Expires=86400&X-Amz-Signature=7cd990476a4e785438b7133e45ce29cc497e38b6f49d435985dd214ba8f40662&X-Amz-SignedHeaders=host'
a = time.time()
r = requests.get(s3_url, stream=True)
b = time.time()
print b-a
if r.status_code == 200:
	with open('../src/s3ZipFile/{0}_{1}.zip'.format(token, sessionId), 'wb') as output:
		output.write(r.content)

	with zipfile.ZipFile('../src/s3ZipFile/{0}_{1}.zip'.format(token, sessionId), 'r') as zf:
		print 1
	 	zf.extractall(pwd='virus', path='../src/s3File/{0}_{1}/{2}'.format(token, sessionId, seq))
        
	for file in os.listdir('../src/s3File/{0}_{1}/{2}'.format(token, sessionId, seq)):
		if file.endswith(".jpg"): 
	 		print file
	 		break
else:
	print None 
		#input_zip = zipfile.ZipFile(r.content)
		#print sys.getsizeof(r.content)
"""	
	with zipfile.ZipFile('../s3ZipFile/{0}_{1}.zip'.format(token, sessionId), 'r') as zf:
		zf.extractall(pwd='virus', path='../s3File/{0}_{1}/{2}'.format(token, sessionId, seq))		
	
	c = time.time()
	for file in os.listdir('../s3File/{0}_{1}/{2}'.format(token, sessionId, seq)):
		if file.endswith(".jpg"): 
			print file
			break
		"""
