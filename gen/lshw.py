# analyze lshw

import subprocess
import re
import os
import sys



class lshw:
   def __init__(self):
      print("Initializing")

   def getText(self, cmd):
	data = subprocess.Popen(['lshw'], stdout=subprocess.PIPE)
	outp,err = data.communicate()
        print(err)
        out = outp.split('\n')
        return out





lh = lshw()
tstr = lh.getText('lshw')
print(tstr[:10])
