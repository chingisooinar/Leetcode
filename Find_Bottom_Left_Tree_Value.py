# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        l_count = 0
        next_count = 0
        stop = 1
        val = 0
        while q:
            node = q.pop(0)
            l_count += 1
            if node.left:
                q.append(node.left)
                next_count += 1
            if node.right:
                q.append(node.right)
                next_count += 1
            if l_count == 1:
                val = node.val
            if l_count == stop and next_count != 0:
                l_count = 0
                stop = next_count
                next_count = 0
        return val
        
        
