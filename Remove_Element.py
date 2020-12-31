class Solution:
    def binarySearch(self,  nums: List[int], val: int) -> int:
        left = 0 
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right)//2
            if(nums[mid] == val):
                if(mid != 0 and nums[mid - 1] == val):
                    while mid - 1 >= 0 and nums[mid - 1] == val:
                        mid -= 1
                return mid
            elif val > nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        return -1
    
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        index = self.binarySearch(nums,val)     #search for the first occurence
        if(index == -1):                        #if a value does not exist, return original length
            return len(nums)
        while index <= len(nums)-1 and nums[index] == val: #keep popping until all occurences are deleted 
            nums.pop(index)
              
        return len(nums)
        
