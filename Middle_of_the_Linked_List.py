# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import math
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        memo = {}
        count = 0
        cur = head 
        while cur:
            memo[count] = cur
            cur = cur.next
            if cur:
                count += 1
        mid = math.ceil(count / 2)
        return memo[mid]
        
            
