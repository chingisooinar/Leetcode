class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=0
        for i in range(len(nums)):
            if(count==0):
                temp=nums[i]
            if(nums[i]==temp):
                count+=1
                if(count==3):
                    count=0
            else:
                return temp
        return nums[len(nums)-1]
