# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        prev = None
        cur = head
        count = 1
        while cur:
            if count % 2 == 0:
                temp = cur.val
                cur.val = prev.val
                prev.val = temp
            prev = cur
            cur = cur.next
            count += 1         
        return head
            
