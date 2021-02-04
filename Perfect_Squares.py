from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n)) == sqrt(n):
            return 1
        sqrs = []
        memo = [0] * (n+1)
        for i in range(1,n+1):
            if int(sqrt(i)) == sqrt(i):
                memo[i] = 1
                sqrs.append(i)
            else:
                mi = n+1
                for sqr in sqrs:
                    if memo[i - sqr] + 1 < mi:
                        mi = memo[i - sqr] + 1
                memo[i] = mi
        return memo[-1]
