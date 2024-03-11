

def product_except(nums):
        n = len(nums)
        arr = [0] * n
        prf = [0] * n
        pst = [0] * n

        prf[0] = 1
        for num in range(1, n):
            prf[num] = nums[num-1] * prf[num-1]
                
        pst[n-1] = 1
        for num in range(n-2, -1, -1):
            print(num)
            pst[num] = nums[num+1] * pst[num+1]

        for ind in range(0, n):
            arr[ind] = prf[ind]*pst[ind]
        return arr

        
