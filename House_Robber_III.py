# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def postorder(node):
            if not node:
                return [0, 0]
            else:
                left_tree = postorder(node.left)
                right_tree = postorder(node.right)
                withRoot = node.val +  left_tree[1] + right_tree[1]
                withoutRoot = max(left_tree) + max(right_tree)
                return [withRoot, withoutRoot]
        return max(postorder(root))
            
        
            
             
