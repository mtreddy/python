
import pandas as pd
import os
import sys



df = pd.read_csv("./tstat_cores64_7763.csv", delimiter='\t')
print(df.shape)
print(len(df))
cnt = 0
ind = int((len(df)+1)/18)
print(ind)
idle=1
busy=0
cidle=0
cbusy=0
tcnt=0

for idx in range(1,ind):
	tind=18*idx-1
	if (df.loc[tind][0] == 'Package'):
		cnt = cnt + 1
		fr = df.loc[tind+2:tind+17]['Busy%'].astype(float)
		#print(fr)
		#print(len(fr),fr.mean())
		#if idx == 500:
		#	break
## Check for transistions from idel to busy or busy to idle and incrment the countr
## Idea is to separate the frames and save as separate files for individual tests
		if fr.mean() > 80 :
			busy = 1
			idle = 0;
			cbusy = cbusy + 1
			if cidle != 0:
				#tcnt = tcnt + 1
				#print("cidle", cidle)
				cidle = 0
		elif fr.mean() < 80 :
			idle = 1
			busy = 0
			cidle = cidle + 1
			if cbusy != 0:
				tcnt = tcnt + 1
				print("cbusy", cbusy)
				cbusy = 0
print("Total %d stats captured" % (cnt))
print("Total %d transistions" % (tcnt))
