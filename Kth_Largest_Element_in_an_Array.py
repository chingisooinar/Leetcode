class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        if k == 0:
            return
        nums.sort()
        return nums[-k]
        
        
