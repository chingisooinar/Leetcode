class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in memo:
                cur = num
                count = 1
                while cur + 1 in memo:
                    cur = cur + 1
                    count += 1
                longest = max(longest, count)
                
                if longest >= len(memo):
                    return longest
        return longest
        
