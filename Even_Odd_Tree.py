# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = 0
        last_even = float('inf')
        last_odd = -float('inf')
        queue = [root]
        prev_level = 0
        count = 0
        bcount = 1
        while queue:
            node = queue.pop(0)
            bcount -= 1
            
            if level != prev_level:
                last_even = float('inf')
                last_odd = -float('inf')
            if level % 2 == 1:
                if node.val < last_even and node.val % 2 == 0:
                    last_even = node.val
                    if node.left:
                        count += 1
                        queue.append(node.left)
                    if node.right:
                        count += 1
                        queue.append(node.right)
                else:
                    return False
            elif level % 2 == 0:
                if node.val > last_odd and node.val % 2 == 1:
                    last_odd = node.val
                    if node.left:
                        count += 1
                        queue.append(node.left)
                    if node.right:
                        count += 1
                        queue.append(node.right)
                else:
                    return False
            prev_level = level
            if bcount == 0:
                level = level + 1
                bcount = count
                count = 0
            
        return True
        
