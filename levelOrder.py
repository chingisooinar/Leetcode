"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        levels = [[]]
        q = [root]
        count = 1
        next_c = 0
        while q:
            node = q.pop(0)
            levels[-1].append(node.val)
            count -= 1
            for child in node.children:
                if child:
                    next_c += 1
                    q.append(child)
                    
            if count == 0:
                if next_c != 0:
                    levels.append([])
                count = next_c
                next_c = 0
        return levels
        
