class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tagret = 0
        out = []
        prev = 0
        for i in range(len(nums)):
            target = 0-nums[i]
            if i>0 and target == prev:
                continue
            prev = target
            left = i+1
            right = len(nums)-1
            while(left<right):
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                if nums[right] + nums[left] == target:
                    li = [nums[right],-target,nums[left]]
                    out.append(li)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                if nums[right] + nums[left] > target:
                    right -= 1
                else:
                    left += 1
        return out
