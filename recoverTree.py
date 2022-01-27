# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        stack = [] # initialize stack
        done = 0
        prev_node = None
        node1 = None
        node2 = None
        while True:

            # Reach the left most Node of the current Node
            if current is not None:

                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                #prev_node = current
                current = current.left


            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif(stack):
                current = stack.pop()
                if prev_node and node1 is None and current.val < prev_node.val:
                    node1 = prev_node
                    node2 = current
                elif prev_node and node1 and current.val < prev_node.val:
                    node2 = current
                prev_node = current

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break
        if node1:
            t = node1.val
            node1.val = node2.val
            node2.val = t
            
