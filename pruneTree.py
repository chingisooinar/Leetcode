# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def hasOne(node):
            if node is None:
                return False
            left = hasOne(node.left)
            right = hasOne(node.right)
            if not left: node.left = None
            if not right: node.right = None
                
            return node.val == 1 or left or right
        return root if hasOne(root) else None
        
