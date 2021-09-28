class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        def find_pos(num, array):
            left = 0
            right = len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] >= num and (mid == 0 or array[mid - 1] < num):
                    return mid
                elif array[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        res = []
        for num in nums:
            if len(res) == 0 or num > res[-1]:
                res.append(num)
            else:
                idx = find_pos(num, res)
                res[idx] = num
        return len(res)
                
