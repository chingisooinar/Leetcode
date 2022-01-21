# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        nums = []
        cur = head
        while cur:
            nums.append(cur.val) # get all vals
            cur = cur.next
        mid_idx = len(nums) // 2 # mid element is the root

        def insert_tree(node, val):
            if node.val < val and node.right is None:
                node.right = TreeNode(val)
            elif node.val > val and node.left is None:
                node.left = TreeNode(val)
            elif node.val < val:
                insert_tree(node.right, val)
            else:
                insert_tree(node.left, val)
    
        def solve(node, nums):
            if len(nums) != 0:
                mid_idx = len(nums) // 2
                insert_tree(node, nums[mid_idx]) # keep inserting middle element
                solve(node, nums[mid_idx + 1:])
                solve(node, nums[:mid_idx])

        root = TreeNode(nums[mid_idx])
        solve(root, nums[mid_idx+1:])
        solve(root, nums[:mid_idx])
        
        return root
            
        
        
