# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = [-float('inf')]
        def inorder(node):
            if not node:
                return True
            res_l = inorder(node.left)
            if node.val > prev[0]:
                prev[0] = node.val
                res = True
            else:
                res = False
            res_r = inorder(node.right)
            return  res_l and res and res_r
        
        return inorder(root)
        
