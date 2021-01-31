"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        root = None
        prev = None
        nodes = []
        og_nodes = []
        while cur:
            node = Node(0)
            node.val = cur.val
            node.random = None
            node.next = None
            if cur == head:
                root = node
            if prev:
                prev.next = node
            og_nodes.append(cur)
            cur = cur.next
            prev = node
            nodes.append(node)
            
        cur = head
        for i in range(len(nodes)):
            if cur.random:
                idx = og_nodes.index(cur.random)
                nodes[i].random = nodes[idx]
                
            cur = cur.next
                
        
        return root
        
