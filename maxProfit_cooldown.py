class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Recursion states:
        i - day
        holding - whether we possess a stock
        cooldown - True or false

        Recursion solution
        def dp(i, cooldown, holding):
            # base case
            if i == len(prices):
                return 0
            if cooldown:
                return dp(i + 1, False, holding)
            elif holding:
                return max(dp(i + 1, cooldown, holding), prices[i] + dp(i + 1, True, False))
            else:
                return max(dp(i + 1, cooldown, holding), -prices[i] + dp(i + 1, cooldown, True))
            
        return dp(0, False, False)
        '''
        n = len(prices)
        dp = [[[0, 0] for _ in range(2)] for _ in range(n + 1)]
        # iterate from the base case
        for i in range(n - 1, -1, -1):
            for cooldown in range(2):
                for holding in range(2):
                    if cooldown:
                        dp[i][cooldown][holding] = dp[i + 1][cooldown - 1][holding]
                    else:
                        do_nothing =  dp[i + 1][cooldown][holding] 
                        if holding:
                            # sell stock
                            do_something = prices[i] + dp[i + 1][1][0]
                        else:
                            # buy stock
                            do_something = -prices[i] + dp[i + 1][cooldown][1]
                        # what is better?
                        dp[i][cooldown][holding] = max(do_nothing, do_something)
        return dp[0][0][0]
