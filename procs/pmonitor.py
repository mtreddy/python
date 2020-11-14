import subprocess
import os
import sys
import time
import threading
import re

lines=[]
def output_reader(proc):
	for line in iter(proc.stdout.readline,b''):
		#print('got line: {0}'.format(line.decode('utf-8')), end='')
		line = format(line.decode('utf-8'))
		#print(line)
		lines.append(line)
	#print(lines)
	return lines

def get_details(lines):
	for line in lines:
		match = re.search('^Copy:', line)
		if match != None:
			print(line)
		match = re.search('^Scale:', line)
		if match != None:
			print(line)
		match = re.search('^Add:', line)
		if match != None:
			print(line)
		match = re.search('^Triad:', line)
		if match != None:
			print(line)

#proc = subprocess.Popen(['vmstat', '5', '5'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc = subprocess.Popen(['./run_stream.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

th = threading.Thread(target=output_reader, args=(proc,))
th.start()
#time.sleep(5)
#proc.terminate()
proc.wait()
get_details(lines)


