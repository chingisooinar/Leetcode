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
        stack.append([root, 1])
        count = 0
        #check = []
        while stack:
            node, level = stack.pop()
            if node == None:continue
            if level > len(path):
                path.append(node.val)
            else:
                path[level-1] = node.val
            
            if node.val >= max(path[ :level]):
                count += 1
                #check.append(node.val)
            stack.extend([[node.left, level+1], [node.right, level+1]])    
        return count
        
