class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        down=up=1
        if(len(nums)<2):
            return len(nums)
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                if(nums[i-1]>nums[i]):
                    down=up+1
                else:
                    up=down+1
        return max(down,up)
