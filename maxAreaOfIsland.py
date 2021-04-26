class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        max_area = 0
        stack = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    area = 0
                    grid[i][j] = -1
                    while stack:
                        x, y = stack.pop()
                        area += 1
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if abs(dx) != abs(dy) and x + dx >= 0 and x + dx < len(grid) and  y + dy >= 0 and y + dy < len(grid[0]) and grid[x + dx][y + dy] == 1:
                                    stack.append((x + dx, y + dy))
                                    grid[x + dx][y + dy] = -1
                                    
                    if area > max_area:
                        max_area = area
        
        return max_area
                                    
