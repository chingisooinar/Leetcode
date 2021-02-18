class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        def rob_I(nums):
            rob1, rob2 = 0, 0
            #[rob1, rob2, n, n+1, ...]
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob_I(nums[:-1]), rob_I(nums[1:]))
