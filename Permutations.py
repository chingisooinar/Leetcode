class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # If length is 1, just return itself
        if len(nums) <= 1:
            return [nums]
        # if length is 2, return both original and reverse
        if len(nums) == 2:
            return [nums, nums[::-1]]
    
    
        res = []
        for i in range(len(nums)):
            res += [x + [nums[i]] for x in self.permute([nums[j] for j in range(len(nums)) if j != i])]
        return res
        
