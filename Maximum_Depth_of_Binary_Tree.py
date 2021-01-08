# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxDepth(self, node):
        if node == None:
            return 0
        return max(1+self.getMaxDepth(node.left), 1+self.getMaxDepth(node.right))
    def maxDepth(self, root: TreeNode) -> int:
        #return self.getMaxDepth(root) uncomment for recursion solution
        queue = []
        queue.append([root,1])
        maxd = 0
        while queue:
            node, d = queue.pop(0)
            if node != None:
                if d > maxd:
                    maxd = d
                queue.append([node.left, d+1])
                queue.append([node.right, d+1])
        return maxd
