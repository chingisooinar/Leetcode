# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        left = 0
        right = 1
        res = 0
        stack = [(root, -1, 0)]
        while stack:
            node, direction, count = stack.pop()
            end = True
            if direction == left and node.left is not None:
                stack.append((node.left, right, count + 1))
                end = False
            elif direction == right and node.right is not None:
                stack.append((node.right, left, count + 1))
                end = False
            
            if direction != left and node.left is not None:
                stack.append((node.left, right, 1))
            if direction != right and node.right is not None:
                stack.append((node.right, left, 1))

            if end and count > res:
                res = count
        return res
            
        
