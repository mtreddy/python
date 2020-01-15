import subprocess
import sys
import os
import re

clist = {}
res = subprocess.check_output(['numactl','-H'])
ln = res.split('\n')
val  = ln[0].split(":")
ccnt = re.findall(r'\d+', val[1]);
cpus = int(ccnt[0])
print("cpus= %s" % (cpus))

for line in ln:
  if len(re.findall(r'node \d+ cpus', line)) != 0:
     tmp = line.split(":")
     cpu = re.findall(r'\d+', tmp[0])
     clist[cpu[0]] = tmp[1] 

print(clist)

keys = sorted(clist.keys())

##bind1   = numactl -m 0  --physcpubind=1
slist = []
cnt = 0
for node in keys:
   cpulist = clist[node].split()
   for cpu in cpulist:
       tstr = "bdin%s = numactl -m %s --physcpubind=%s" % (cnt, node, cpu)
       print(tstr)
       cnt+=1
    

       


