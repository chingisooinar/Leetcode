# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def insert(nums):
            if not nums or len(nums) == 0:
                return None
            idx = nums.index(max(nums))
            node = TreeNode(val=nums[idx])
            node.right = insert(nums[idx+1:])
            node.left = insert(nums[:idx])
            return node
        root = insert(nums)
        return root
