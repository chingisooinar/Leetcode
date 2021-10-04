# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        memo = {}
        idx = 0
        cur = head
        while cur:
            if cur not in memo.keys():
                memo[cur] = idx
            else:
                return cur
            idx += 1
            cur = cur.next
        return None
            
        
