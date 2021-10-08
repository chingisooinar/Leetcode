class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        memo[1] = 1
        
        def solve(n, memo):
            if n in memo.keys():
                return memo[n]
            total = 0
            
            # solve(i - 1, memo) - left subtree
            # solve(n - i, memo) - right subtree
            for i in range(1, n + 1):
                total += solve(i - 1, memo) * solve(n - i, memo) # cartesian product
            memo[n] = total
            return total
            
        return solve(n, memo)
        
