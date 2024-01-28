
#Using fermats little theorem
def is_prime(n):
    if n%2 == 0:
        return False
    if n <= 3:
        return True
    a = 4 #Any number
    val = a**(n-1) - 1
    print(val)
    if val%n != 0:
        return False
    else:
        return True
