class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dp = [float('inf') for _ in range(len(seats) + 1)]
        for i in range(1, len(seats) + 1):
            if seats[i - 1] == 1:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + 1
        for i in range(len(seats) - 1, 0, -1):
            if seats[i - 1] == 1:
                dp[i] = 0
            else:
                dp[i] = min(dp[i], dp[i + 1] + 1)
        return max(dp[1:])
        
