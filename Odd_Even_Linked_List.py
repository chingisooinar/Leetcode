# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        f_even = l_even = f_odd = l_odd = None
        cur = head
        count = 1
        while cur:
            if count % 2 == 1:
                if not f_odd and not l_odd:
                    f_odd = cur
                    l_odd = cur
                else:
                    l_odd.next = cur
                    l_odd = cur
            else:
                if not f_even and not l_even:
                    f_even = cur
                    l_even = cur
                else:
                    l_even.next = cur
                    l_even = cur
            count += 1
            cur = cur.next
        l_even.next = None
        l_odd.next = f_even
        return head
