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
cicols = [col for col in pdata.columns if 'CPI (Sys + User)' in col]
uicols = [col for col in pdata.columns if 'Utilization' in col]
cores = len(icols)
print("Number of cores =%d" % cores)
print("Number of rows", len(pdata.index))
tot = [] 
ctot = [] 
utot = [] 
for i in range(len(pdata.index)):
	ser = pdata.loc[i, icols[0:cores]]
	cser = pdata.loc[i, cicols[0:cores]]
	user = pdata.loc[i, uicols[0:cores]]
	avg = (ser.sum()/len(ser.index))
	cavg = (cser.sum()/len(cser.index))
	uavg = (user.sum()/len(user.index))
	#print("Core %d avg cpi=%f max=%f min=%f" % (i, avg, ser.max(), ser.min()))
	tot.append(avg)
	ctot.append(cavg)
	utot.append(uavg)
	
plt.plot(tot)
plt.savefig("ipc.png")
plt.close()	
plt.plot(ctot)
plt.savefig("cpi.png")
plt.close()	
plt.plot(utot)
plt.savefig("util.png")

icols = [col for col in pdata.columns if 'Mem' in col]
cores = len(icols)
print("Number of cores =%d" % cores)
print("Number of rows", len(pdata.index))
tot = [] 
for i in range(len(pdata.index)):
	ser = pdata.loc[i, icols[0:cores]]
    ## we only show the total BW for memory
	msum = ser.sum()
	#print("Core %d avg cpi=%f max=%f min=%f" % (i, avg, ser.max(), ser.min()))
	tot.append(msum)
	
plt.close()	
plt.plot(tot)
plt.savefig("mem.png")


icols = [col for col in pdata.columns if 'Ave L3 Miss Latency' in col]
cores = len(icols)
print("Number of cores =%d" % cores)
print("Number of rows", len(pdata.index))
tot = [] 
for i in range(len(pdata.index)):
	ser = pdata.loc[i, icols[0:cores]]
	avg = (ser.sum()/len(ser.index))
	#print("Core %d avg cpi=%f max=%f min=%f" % (i, avg, ser.max(), ser.min()))
	tot.append(avg)
plt.close()	
plt.plot(tot)
plt.savefig("l3.png")
plt.close()	

