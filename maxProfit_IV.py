class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        Recursion:
        
        def dp(i, remaining, holding):
            if remaining == 0 or i == len(prices):
                return 0
            if holding:
                return max(dp(i + 1, remaining, holding), prices[i] + dp(i + 1, remaining - 1, not holding))
            else:
                return max(dp(i + 1, remaining, holding), -prices[i] + dp(i + 1, remaining, not holding))
        
        return dp(0, k, False)
        '''
        n = len(prices)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for remaining in range(1, k + 1):
                for holding in range(2):
                    do_nothing = dp[i + 1][remaining][holding]
                    if holding:
                        do_something = prices[i] + dp[i + 1][remaining - 1][0]
                    else: 
                        do_something = -prices[i] + dp[i + 1][remaining][1]
                    dp[i][remaining][holding] = max(do_nothing, do_something)
        return dp[0][k][0]
