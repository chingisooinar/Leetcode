class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [float('inf') for _ in nums]
        memo[0] = 0
        for i in range(nums.__len__() - 1):
            for j in range(1, nums[i] + 1):
                if i + j < nums.__len__():
                    memo[i + j] = min(memo[i] + 1, memo[i + j])
        return memo[-1]
