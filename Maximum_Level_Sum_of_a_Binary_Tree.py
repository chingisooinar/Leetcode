# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        queue = [root]
        count = 0
        bcount = 1
        summ = 0
        maxsum = -1
        maxlevel = 1
        while queue:
            node = queue.pop(0)
            summ += node.val
            
            if node.left:
                count += 1
                queue.append(node.left)
                
            if node.right:
                count += 1
                queue.append(node.right)
            
            bcount -= 1
            if bcount == 0:
                if level == 1:
                    maxsum = summ
                elif summ > maxsum:
                    maxsum = summ
                    maxlevel = level
                level += 1
                bcount = count
                count = 0
                summ = 0
        return maxlevel
            
