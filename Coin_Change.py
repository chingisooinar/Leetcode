class Solution:
    def getChange(self, coins, amount, memo):
        if amount < 0:return -1
        if amount == 0:return 0
        if amount-1 >= 0 and amount-1<len(memo) and memo[amount - 1]!=0:return memo[amount - 1]
        min_ = float("inf")
        for i in coins:
            res = self.getChange(coins, amount - i, memo)
            if res>=0 and min_>res:
                min_ = res + 1
        memo[amount - 1] = min_ if min_!=float("inf") else -1
        return memo[amount - 1]
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        return self.getChange(coins, amount, [0]*amount)
