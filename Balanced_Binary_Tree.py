# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkHeight(self,node,func=None):
        if node == None:
            return 0
        return func(1 + self.checkHeight(node.right,func=func), 1 + self.checkHeight(node.left,func=func))
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return abs(self.checkHeight(root.left, func=max) - self.checkHeight(root.right, func=max)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
