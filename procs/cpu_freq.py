import os
import re
import sys
import subprocess
import time
import datetime as dt



cpu_id=0
#tstr="/home/amd/src/amd/tools/avt/AVT_Linux_NDA_2.7.14/AVTCMD -module pstates getcorepstate(%d)" % (cpu_id)
#cmd=tstr.split(" ")
#print(cmd)

fl = "cpu_freq_log"+str(dt.datetime.now())+".txt"
fl = fl.replace(' ', '')
fd = open(fl,"w")
while 1:
        cpu_id=cpu_id%64
        print(cpu_id)
        fd.write("cpu_id %d\n" % (cpu_id))
        tstr="/home/amd/src/amd/tools/avt/AVT_Linux_NDA_2.7.14/AVTCMD -module pstates getcorepstate(%d)" % (cpu_id)
        print(tstr)
        fd.write(tstr)
        cmd=tstr.split(" ")
        err = subprocess.run(cmd,capture_output=True)
        sstr1 = err.stdout.decode()
        fd.write(sstr1)
        #print(sstr1)
        errs = sstr1.split(',')
        #print(errs)

        val=int(re.findall(r'\d+',errs[3])[0])
        print(val)
        if val <  int(1300):
           fd.write("Error: Freq is below threshold %d" % (val))
        time.sleep(5)
        cpu_id=cpu_id+1

