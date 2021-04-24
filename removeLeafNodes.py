# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)            
            check = [child for child in [node.left, node.right] if child is None or child.val == -1]
            if len(check) == 2 and node.val == target:
                node.val = -1
            if node.left and node.left.val == -1:
                node.left = None
            if node.right and node.right.val == -1:
                node.right = None
            

        helper(root)
        return root if root is not None and root.val != -1 else None
            
        
