#!/usr/bin/python
import sys
import shutil
import pandas as  pd

print(sys.argv[1])
dst = "./tmp.csv"
shutil.copyfile(sys.argv[1], dst)
pdata = pd.read_csv(dst, sep=',',skiprows=34)
icols = [col for col in pdata.columns if 'Umc' in col]
#print(ser)
#print(ser.sum())
#print(len(pdata.columns))
ncores =128
#cores =int( (len(pdata.columns)-1)/17)
cores = len(icols)
print("Number of cores =%d" % cores)
print("Number of rows", len(pdata.index))
for i in range(cores):
	#print(pdata.columns[i*17+3])
	#ser = pdata[pdata.columns[i*17+3]]
	#avg = (ser.sum()/len(pdata.index))
	ser = pdata[icols[i]]
	#print(type(ser))
	#print(ser)
	avg = (ser.sum()/len(ser.index))
	print("Memory controller:%d avg mem BW:%f" % (i, avg))
