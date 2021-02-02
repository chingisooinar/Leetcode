# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        count = 0
        mi = float('inf')
        while stack or cur:
            if cur:
                stack.append(cur)
                cur =  cur.left
            elif stack:
                cur = stack.pop()
                count += 1
                if count == k:
                    return cur.val
                cur = cur.right
        return -1
        
