class fibnum:
 def __init__(self):
    self.dp = []
    self.dp.append(0)
    self.dp.append(1)
    self.dp.append(1)
 def fibn(self, num):
    if num <= 0:
        return 0
    elif num == 1 or num == 2 :
        return 1
    if num not in range(len(self.dp)):
        val = self.fibn(num-1) + self.fibn(num-2)
        self.dp.append(val)
        return val
    else:
        return self.dp[num]



fb = fibnum()
fb.fibn(10)
print(fb.dp)
