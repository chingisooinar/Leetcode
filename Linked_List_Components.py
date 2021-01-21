# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        cur = head 
        hit_c = 0
        while cur:
            if cur.val in G:
                hit_c += 1
            else:
                if hit_c !=0:count+=1
                hit_c = 0
            cur = cur.next
        if hit_c !=0:count+=1

        return count
