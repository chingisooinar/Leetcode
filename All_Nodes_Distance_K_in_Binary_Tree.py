# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        
        queue = [(target,0)]
        visited = [target]
        while queue:
            if queue[0][1] == K:
                return [node.val for node, dis in queue if dis == K]
            node, dis =  queue.pop(0)
            for adj in [node.left,node.right,node.par]:
                if adj and adj not in visited:
                    visited.append(adj)
                    queue.append([adj,dis+1])
        return []
