class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0 
        left = 0
        ones = 0
        for right, digit in enumerate(nums):
            # count ones within current window
            ones += digit
            # (right - left + 1) -> window length
            # window length - ones = # of zeros
            # if # of zeros > k -> move window to the left and update ones
            while (right - left + 1) - ones > k:
                ones -= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
        return res
                
            
        
