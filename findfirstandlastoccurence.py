class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums)==1 and target==nums[0]):
            return [0,0]
        first=0
        last=len(nums)-1
        while(first<=last):
            mid=(first+last)//2
            if(target>nums[mid]):
                first=mid+1
            elif(target<nums[mid] or (mid>0 and target==nums[mid-1])):
                last=mid-1
                continue
            if(target==nums[mid]):
                print(mid,last)
                end=mid
                i=mid+1
                while(i<len(nums) and target==nums[i]):
                    end=i
                    i+=1
                return [mid,end]
            
        return [-1,-1] 
