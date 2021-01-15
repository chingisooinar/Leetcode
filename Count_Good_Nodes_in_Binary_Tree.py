# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        path = []
        stack.append([root, root.val])
        count = 0
        while stack:
            node, level = stack.pop()
            if node == None:continue
            if node.val >= level:
                count += 1
                stack.extend([[node.left, node.val], [node.right, node.val]]) 
            else:
                stack.extend([[node.left, level], [node.right, level]])
        return count
        
