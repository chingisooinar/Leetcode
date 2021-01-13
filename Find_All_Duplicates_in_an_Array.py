class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                out.append(nums[i])
        return out
