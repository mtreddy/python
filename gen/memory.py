#!/usr/bin/python
import sys
import shutil
import pandas as  pd

print(sys.argv[1])
dst = "./tmp.csv"
shutil.copyfile(sys.argv[1], dst)
pdata = pd.read_csv(dst, sep=',',skiprows=42)
icols = [col for col in pdata.columns if 'Mem' in col]
ncores =128
cores = len(icols)
print("Number of cores =%d" % cores)
print("Number of rows", len(pdata.index))
tot = [] 
for i in range(cores):
	ser = pdata.loc[i, icols[0:cores]]
	avg = (ser.sum()/len(ser.index))
	#print("Core %d avg cpi=%f max=%f min=%f" % (i, avg, ser.max(), ser.min()))
	tot.append(avg)
	
#plt.savefig("ipc.fig")

'''
for i in range(cores):
	ser = pdata[icols[i]]
	avg = (ser.sum()/len(ser.index))
	print("Memory controller:%d avg mem BW:%f" % (i, avg))
	'''
