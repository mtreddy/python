#!/usr/bin/python
import sys
import shutil
import pandas as  pd
import matplotlib.pyplot as plt

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
tot = [] 
for i in range(len(pdata.index)):
	##This is per row at a time 
	ser = pdata.loc[i, icols[0:cores]]
	avg = (ser.sum()/len(ser.index))
	#print("Core %d avg cpi=%f max=%f min=%f" % (i, avg, ser.max(), ser.min()))
	tot.append(avg)
	
plt.plot(tot)
plt.savefig("ipc.png")

'''
for i in range(cores):
	ser = pdata[icols[i]]
	avg = (ser.sum()/len(ser.index))
	print("Core %d avg cpi=%f" % (i, avg))
	'''
