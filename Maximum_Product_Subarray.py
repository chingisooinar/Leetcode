class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cur_max = cur_min = 1
        res = - float('inf')
        for n in nums:
            tmp = cur_min
            cur_min = min(cur_min * n, n, cur_max * n)
            cur_max = max(tmp * n, n, cur_max * n)
            res = max(res, cur_max)
            
        return res
