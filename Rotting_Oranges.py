class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        Q = []
        memo = []
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        # calculate fresh oranges and push rotten oranges into Q
        for i in range(n):
            memo.append([])
            for j in range(m):
                if grid[i][j] == 2:
                    memo[i].append(1)
                    Q.append((i, j))
                else:
                    if grid[i][j] == 1:
                        fresh += 1
                    memo[i].append(0)
        pushed = len(Q)
        # if there are no fresh, then 0
        if fresh == 0:
            return 0
        
        while Q:
            i, j = Q.pop(0)
            pushed -= 1
            for ix in range(-1, 2):
                for jx in range(-1, 2):
                    if abs(ix) != abs(jx) and i + ix >= 0 and i + ix < n and j + jx >= 0 and j + jx < m:
                        if memo[i + ix][j + jx] == 0 and grid[i + ix][j + jx] == 1:
                            Q.append((i + ix, j + jx))
                            memo[i + ix][j + jx] = 1
                            fresh -= 1
                    
            if pushed == 0 and len(Q):
                minutes += 1
                pushed = len(Q)
        # if there are some fresh oranges remaining, then -1                    
        if fresh != 0:
            return -1
        return minutes
