# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        parent = None
        while cur:
            parent = cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        newnode = TreeNode(val = val)
        if parent:
            
            if parent.val < val:
                parent.right = newnode
            else:
                parent.left = newnode
        else:
            return newnode
        return root
        
