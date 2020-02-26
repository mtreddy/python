#!/usr/bin/python
"""
  This code to analyze systems based on jason file provided

  CPU diag: 
   a. Number of cores
   b. SMT enabled or not?
   c. CPU frequency
   d. Power state

  Memory:
  a. Size of the memory
  b. Memory organization
  c. Speed (clk)
  d. 
  
  PCIe
  a. Number of bus
  b. Bus speed

"""
import subprocess
import sys
import os
import re


class sysdiag:
   def cpu_diag(self, cpustr):
       res = subprocess.check_output(['lscpu'])
