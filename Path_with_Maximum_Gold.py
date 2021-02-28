class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                stack = [(i,j, [(i,j)],grid[i][j])]
                while stack:
                    x, y,path, d = stack.pop()
                    res = max(res, d)
                    for x1, y1 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= x1 < m and 0 <= y1 < n and (x1,y1) not in path and grid[x1][y1] != 0:
                            stack.append((x1, y1,path + [(x1,y1)], d + grid[x1][y1]))
        return res
