# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def insert(node, val):
            if node.val < val:
                if node.right == None:
                    new = TreeNode(val)
                    node.right = new
                else:
                    insert(node.right, val)
            elif node.val > val:
                if node.left == None:
                    new = TreeNode(val)
                    node.left = new
                else:
                    insert(node.left, val)
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            insert(root, preorder[i])
        return root
