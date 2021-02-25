# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        def post(node,cur_max,cur_min):
            if node:
                cur_max = max(cur_max, node.val)
                cur_min = min(cur_min, node.val)
                left = post(node.left, cur_max, cur_min)
                right = post(node.right, cur_max, cur_min)
                return max(left, right)
                
            else:
                return cur_max - cur_min
        return post(root, root.val, root.val)
