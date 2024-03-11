def duplicate(nums):
    tbl = defaultdict(int)
    for ind in range(0,len(nums)):
        if nums[ind] in tbl.keys():
            return True
        else:
            tbl[nums[ind]] = 1
    return False
