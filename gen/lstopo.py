import sys
import os
import re
import subprocess

class lstopo:
  def __init__(self):
    print("Initializing")
    self.cmd = "lstopo-no-graphics"


  def analyze(self):
      op = subprocess.check_output(self.cmd)
      lines = op.split("\n")
      L3 = {}
      thrp = {}
      l3 = ''
      cr = []
      for line in lines:
        if line.find("L3") >= 1:
           tt = re.findall(r'L#\d+',line)
           l3 = re.findall(r'\d+',tt[0])[0]  
           print("L3",l3)
           L3[l3] = []
        elif line.find("Core L#") >= 1:
           tt = re.findall(r'Core L#\d+', line)
           cr = re.findall(r'\d+',tt[0])[0]  
           print("CPU", cr)
           L3[l3].append(cr)
           thrp[cr] = []
        else:
           if line.find("GPU L") >= 1 :
              continue
           elif line.find("PU L") >= 1 :
              th = re.findall(r'P#\d+', line)
              print(th)
              thrp[cr].append(th[0])
      return L3
 

lst = lstopo()
val = lst.analyze()
print(val)
           
           
