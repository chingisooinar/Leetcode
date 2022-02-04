class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        '''
        Recursion:
        states:
        i - 
        built -
        
        def dp(i, built):
            base solution:
            if built == k - 1:
                return sum(nums[i:]) / (len(nums[i:]))
            max_ = 0
            for j in range(i, len(nums)):
                avg = sum(nums[i:j]) / len(nums[i:j]) if len(nums[i:j]) != 0 else 0
                max_ = max(avg + dp(j, built + 1), max_)
            return max_
        return dp(0, 0)
        '''
        n = len(nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(k)]
        # initialize base solution
        for i in range(n): 
            dp[k - 1][i] = sum(nums[i:]) / (n - i)
        # iterate from base solution
        for built in range(k - 2, -1, -1):
            for i in range(n + 1):
                max_ = 0
                for j in range(i, n + 1):
                    avg = sum(nums[i:j]) / (j - i) if j - i != 0 else 0
                    max_ = max(avg + dp[built + 1][j], max_)
                dp[built][i] = max_
        return dp[0][0]
