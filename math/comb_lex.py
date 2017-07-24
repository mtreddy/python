import numpy
def print_comb(arr, barr):
    i = len(arr) - 1
    while i >= 0:
        if arr[i] == 1:
            print(barr[i])
        i -= 1
def comb_lex(arr, carr):
    ind = 0
    n = len(arr)
    print(n)
    print(2**n)
    while ind < 2**n:
        print(arr)
        print_comb(arr, carr)
        i = n - 1
        while arr[i] == 1 and i >= 0:
            arr[i]=0
            i -= 1
        arr[i] = 1
        ind += 1

arr = [0,0,0,0]
barr = [1,2,3,4,5]
comb_lex(arr, barr)
