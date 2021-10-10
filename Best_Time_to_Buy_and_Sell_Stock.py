class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float('inf')
        for val in prices:
            minprice = min(minprice, val)
            maxprofit = max(maxprofit, val - minprice)
        return maxprofit
