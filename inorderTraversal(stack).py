# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur=root
        prev=None
        res=[]
        stack=[cur]
        tack=[]
        while(len(stack) and root!=None):
            if(stack[-1].left!=None and stack[-1].left not in tack):
                stack.append(stack[-1].left)
            else:
                node=stack.pop()
                res.append(node.val)
                tack.append(node)
                
                if(node.right!=None and node.right not in tack):
                    stack.append(node.right)
        return(res)
