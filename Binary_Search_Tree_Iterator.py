# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.rootPtr = root
        self.cur = root
        self.stack = []

    def next(self) -> int:
        while True:
            if self.cur is not None:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            elif self.stack:
                self.cur = self.stack.pop()
                val = self.cur.val
                self.cur = self.cur.right
                return val

    def hasNext(self) -> bool:
        return self.cur is not None or self.stack 
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
