# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(node):
            prev = None
            cur = node
            fast = node.next
            while fast:
                cur.next = prev
                prev = cur
                cur = fast
                fast = fast.next
            cur.next = prev
            return cur
        fast = reverse(slow.next)
        slow.next = None
        
        slow = head
        while fast:
            temp = fast.next
            fast.next = slow.next
            slow.next = fast
            slow = fast.next
            fast = temp
        return head
