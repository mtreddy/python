
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mprof = 0
        #prof = 0
        buy = 0
        sell = 1
        while(sell < len(prices)):
            if prices[buy] < prices[sell]:
                prof = prices[sell] - prices[buy]
                mprof = max(prof, mprof)
            else:
                buy = sell
            sell +=1
        return mprof


prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
sl = Solution()
print(sl.maxProfit(prices))
