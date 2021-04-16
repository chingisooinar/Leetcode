class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        init_sum = 0
        max_sum = 0
        for num in nums:
            init_sum += num
            max_sum = max(init_sum, max_sum)
            init_sum = max(0, init_sum)
        if min(nums) < 0 and max(nums) < 0:
            return max(nums)
        if max(nums) > max_sum:
            return max(nums)
                
        return max_sum
        
