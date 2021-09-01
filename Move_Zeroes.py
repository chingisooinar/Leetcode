class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = right = len(nums) - 1
        while left != -1:
            num = nums[left]
            if num != 0:
                left -= 1
            else:
                if left == right:
                    left -= 1
                    right -= 1
                else:
                    for i in range(left, right):
                        nums[i] = nums[i + 1]
                    nums[right] = 0
                    right -= 1

