class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0
        coins.sort()
        for i in range(amount + 1):
            for j in range(n):
                if i >= coins[j]:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
                else:
                    break
                     
        return dp[-1] if dp[-1] != amount + 1 else -1
        
  
