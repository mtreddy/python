#!/usr/bin/python
import sys
import shutil
import pandas as  pd

print(sys.argv[1])
dst = "./tmp.csv"
shutil.copyfile(sys.argv[1], dst)
#pdata = pd.read_csv(dst, sep=',',skiprows=34)
pdata = pd.read_csv(dst, sep=',',skiprows=42)
print(pdata.columns)
icols = [col for col in pdata.columns if 'IPC (Sys + User)' in col]
cores = len(icols)
print("Number of cores =%d" % cores)
print("Number of rows", len(pdata.index))
for i in range(cores):
	ser = pdata[icols[i]]
	avg = (ser.sum()/len(ser.index))
	print("Core %d avg cpi=%f" % (i, avg))
