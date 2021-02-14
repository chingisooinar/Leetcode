# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        count = 1
        first = None
        second = None
        cur = head
        memo = []
        while cur:
            if not first and count == k:
                first = cur
            if len(memo) == k:
                memo.pop(0)
            memo.append(cur)
            cur = cur.next
            count += 1
        second = memo[0]
        temp = second.val
        second.val = first.val
        first.val = temp
        return head
                
        
