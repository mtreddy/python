#
import pandas as pd
import os
import sys
import numpy as np


if len(sys.argv) < 2:
	print("Usage:python3 avg_freq <tstat-file>")
avg_freq = 0
cnt = 0
for fds in range(1, len(sys.argv)):
	df = pd.read_csv(sys.argv[1], delimiter="\t")
	tdf=df[df["Busy%"]== "100.00"]
	nfreq=np.array(tdf["Avg_MHz"])
	afreq=nfreq.astype(np.float)
	print("File %s freq %f" % (sys.argv[fds],afreq.mean()))
	cnt = cnt + 1
	avg_freq = avg_freq + afreq.mean()

print("avg_freq=%f" % (avg_freq/cnt))

