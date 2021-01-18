class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def check_if_no_answer(sorted_int_list):
                        # check there can be extra answers in the sorted list
            if len(sorted_int_list) < 3:
                return True

            if sorted_int_list[0] > 0:
                return True

            if sorted_int_list[-1] < 0:
                return True
            return False
    
        nums.sort()
        tagret = 0
        out = []
        prev = 0
        for i in range(len(nums)):
            if check_if_no_answer(nums[i:]):
                return out
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
