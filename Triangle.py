class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = [[0 for _ in range(len(triangle[i]))] for i in range(n)]
        memo[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                range_min = j - 1 if j != 0 else j
                range_max = j 
                memo[i][j] = min(memo[i - 1][range_min:range_max + 1]) + triangle[i][j]
        return min(memo[-1])
        
