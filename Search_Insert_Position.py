class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left = 0
        index = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right)//2
            if(nums[mid] == target): # if a target already exists in a list
                return mid
            if(mid + 1 < len(nums) and target <= nums[mid + 1] and target > nums[mid]): # if a target should be placed in between mid and mid + 1
                return mid + 1
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        if mid == len(nums) - 1 and nums[mid] < target: # if target > max value
            return len(nums)
        return 0  #else it is a min value
            
        
