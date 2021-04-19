# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        count = 1
        next_count = 0
        q = [root]
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                next_count += 1
            if node.right:
                q.append(node.right)
                next_count += 1
            count -= 1
            res += node.val
            if count == 0:
                if next_count != 0:
                    res = 0
                count = next_count
                next_count = 0
        return res
