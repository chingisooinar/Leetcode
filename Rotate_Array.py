class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = nums.__len__()
        k = k % N
        memo = [nums[i] for i in range(N)]
        for i in range(N):
            nums[(i + k) % N] = memo[i]
