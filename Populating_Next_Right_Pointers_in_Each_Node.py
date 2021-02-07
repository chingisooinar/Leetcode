"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        prev = None
        bcount = 1
        count = 0
        while queue:
            node = queue.pop(0)
            bcount -= 1
            if prev:
                prev.next = node
            if node.left:
                count += 1
                queue.append(node.left)
            if node.right:
                count += 1
                queue.append(node.right)
            prev = node
            if bcount == 0:
                prev = None
                bcount = count
                count = 0
        return root
            
                
