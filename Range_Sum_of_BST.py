# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        node = root
        stack = []
        res = 0
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val >= low:
                    res += node.val
                if node.val >= high:
                    return res
                node = node.right
