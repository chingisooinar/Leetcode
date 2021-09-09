# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        stack = []
        reverse = None
        while cur:
            stack.append(cur)
            temp = cur.next
            cur.next = None
            cur = temp
            
        while stack:
            node = stack.pop()
            if not reverse:
                reverse = node
                cur = reverse
            else:
                cur.next = node
                cur = node
        return reverse
