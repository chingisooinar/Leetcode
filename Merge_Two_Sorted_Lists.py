# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        cur1 = l1
        cur2 = l2
        curM = merged
        while cur1 or cur2:
            nextNode = None
            if cur1 and cur2 and cur1.val > cur2.val:
                nextNode = cur2
                cur2 = cur2.next
            elif cur1 and cur2 and cur1.val < cur2.val:
                nextNode = cur1
                cur1 = cur1.next
            elif cur1 and not cur2:
                nextNode = cur1
                cur1 = cur1.next
            else:
                nextNode = cur2
                cur2 = cur2.next
            
            if curM is None:
                merged = nextNode
                curM = merged
            else:
                curM.next = nextNode
                curM = nextNode
        return merged
                
            
            
                
        
