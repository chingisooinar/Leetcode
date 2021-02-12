# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if node:
                return [node] + preorder(node.left) + preorder(node.right) 
            else:
                return []
        re_list = preorder(root)
        prev = None
        for node in re_list:
            node.left = None
            node.right = None
            if prev:
                prev.right = node
            prev = node

            
            
