class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        n = len(prices)
        profit = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            
            profit += (peak - valley)
        return profit
