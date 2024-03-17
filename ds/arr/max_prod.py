
def max_prod(nums):
    mprod = 1
    prod = 1
    for num in nums:
        prod = prod * num
        if prod == 0:
            prod = 1
        mprod = max(mprod, prod)
    if mprod == 1:
        return 0
    return mprod
