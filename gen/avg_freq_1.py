#!/usr/bin/python
import os
import sys
import numpy as np
import pandas as pd

#bnames = [astar,bzip2,gcc,gobmk,h264ref,hmmer,libquantum,mcf,omnetpp,perlbench,sjeng,xalancbmk]
if len(sys.argv) < 2:
    print("avg_freq.pyt tstat.csv")
if 1:
## Process getcorefreq stats
    fnum=0
    flist=[]
    for num in range(1,len(sys.argv)):
        df = pd.read_csv(sys.argv[num])
        tdf = df[df[df.columns[6]] >= (100.0)]
        afreq=tdf[tdf.columns[3]]
        arr = np.array(afreq)
        print(arr.mean())
        flist.append(arr.mean())
    nafreq=np.array(flist)
    print("Eff Freq:", nafreq.mean())

else:
## Process turbstats
    fnum=0
    flist=[]
    for num in range(1,len(sys.argv)):
        fd = open(sys.argv[num], 'r')
        line = fd.read()
        lines = line.split("\n")
        count = 0
        freq = 0
        afreq = 0
        for ln in lines:
            tmp = ln.split('\t')
            if len(tmp) > 5:
                #print(tmp)
                if tmp[4] == '100.00':
                    #print(tmp[5])
                    freq=freq+int(tmp[5])
                    count=count+1

        fd.close()
        #print(count, freq)
        print("Avg-freq %f" %(freq/count))
        flist.append(float(freq/count))

    arr = np.array(flist)
    print(arr.mean())

