import math

moves = {}

def movesFn(n):

    if n <= 3:
        return n
    if n in moves.keys():
        return moves[n]
    minv = 0xffffffff
    #find factor
    factor = 1
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            factor = n/i
            minv = min(minv, 1 + movesFn(factor))
    minv = min(minv, 1 + movesFn(n-1))
    moves[n] = minv
    return minv


print(movesFn(2))
print(movesFn(3))
print(movesFn(4))
print(movesFn(5))
print(movesFn(428689))

