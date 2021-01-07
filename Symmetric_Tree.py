# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, node, node2):
        if(node == None and node2 == None):
            return True
        if(node == None or node2 == None):
            return False
        return node.val == node2.val and self.isMirror(node.left,node2.right) and self.isMirror(node.right,node2.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        #return self.isMirror(root,root) uncomment for recursive solution
        queue = []         #BFS approach
        node1 = root
        node2 = root
        queue.append(node1)
        queue.append(node2)
        while(queue):
            node = queue.pop(0)
            node2 = queue.pop(0)
            if(node == None and node2 == None):
                continue
            if(node == None or node2 == None):
                return False       
            if(node.val != node2.val):
                return False
            queue.extend([node.left,node2.right,node.right,node2.left])
        return True
        
