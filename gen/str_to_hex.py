import re
#tt='a056cd15852a6edb0203066006ca55869ee535f0c9a8db8d7a53c1c7168e65ff964b7412e14e0985ddf094d26cdca473234e5fa918fe69dbcd5edc132bf9776e'
tt='1b81934e3ae99d2f02b2e5479de1bd52c911545f7c36889e9a726c7b5ca386d5'

arr = re.findall('..', tt)
ll=[]
ind = 1
for val in arr:
    inp = "0x%s" %  (val)
    ll.append(inp)
ll.reverse()
for val in ll:
    print(",",val, end='')
    if ind%16 ==0:
        print(",")
    ind = ind+1

