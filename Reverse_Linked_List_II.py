# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        nodes = []
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = None
            nodes.append(cur)
            cur = temp
        
        prev = new_head = None
        for i in range(len(nodes)):
            idx = i + 1
            if idx >= left and idx <= right:
                idx = left + right - idx
            
            cur = nodes[idx - 1]
            if prev is None:
                new_head = cur
            else:
                prev.next = cur
            prev = cur
                
        return new_head
