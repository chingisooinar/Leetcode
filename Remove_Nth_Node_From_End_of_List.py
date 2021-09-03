# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        memo = {}
        count = 0
        cur = head 
        while cur:
            memo[count] = cur
            cur = cur.next
            count += 1
        if count-n-1 >=0 and memo[count-n-1]:
            memo[count-n-1].next = memo[count-n].next
            return head
        else:
            return memo[count-n].next
