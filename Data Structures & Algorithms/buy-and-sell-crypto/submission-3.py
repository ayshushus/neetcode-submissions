class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = set()
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j]-prices[i])
            profits.add(profit)
        if max(profits) < 0:
            return 0
        else:
            return max(profits)
        

# brute force
# 1st index on left, 
# compare with everything right
# index - (index on right), store max, for iteration
# redo for all indices, store max of above

