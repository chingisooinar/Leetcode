# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        prev = None
        x = 0
        l3 = None
        while cur1 != None or cur2 != None:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            node = ListNode()
            node.val = (val1 + val2 + x) % 10
            x = 1 if val1 + val2 + x >= 10 else 0
            if prev:
                prev.next = node
            if not l3:
                l3 = node
            prev = node
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        if x:
            node = ListNode()
            node.val = x
            prev.next = node
        return l3
        
        
