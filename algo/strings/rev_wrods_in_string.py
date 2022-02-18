import os
import sys
ts = 'Hello World, here I am'
lts = ts.split()
rts = []
for w in lts:
    tmp = ""
    ln = len(w)
    if ln == 0 or ln == 1:
        rts.append(w)
        continue
    for i in range(0, ln):
        tmp = tmp + w[ln-i-1]
    print(tmp)
    rts.append(tmp)
print(rts)
