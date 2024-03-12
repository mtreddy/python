nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray(nums):
    
    msum = nums[0]
    lsum = 0
    left = 0
    right = 0

    for num in nums:
        lsum = lsum  + num
        if lsum > msum:
            msum = lsum
        if lsum < 0:
            lsum = 0
    return msum
