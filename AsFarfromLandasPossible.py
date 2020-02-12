import math
import copy
def isthere(check,lis):
    if(check==lis):
        return 0
    return 1
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=[]
        res1=[]
        for i in grid:
            res.append(max(i))
            res1.append(min(i))
        if(max(res)==0 or min(res1)==1):
            return -1
        check=[]
        while(isthere(check,grid)):
            check=copy.deepcopy(grid)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if(grid[i][j]==1):
                        continue
                    mi=float('Inf')
                    if(i-1>=0):
                        if(grid[i-1][j]<mi and grid[i-1][j]!=0):
                            mi=grid[i-1][j]
                    if(j-1>=0):
                        if(grid[i][j-1]<mi and grid[i][j-1]!=0):
                            mi=grid[i][j-1]
                    if(i+1<len(grid)):
                        if(grid[i+1][j]<mi and grid[i+1][j]!=0):
                            mi=grid[i+1][j]
                    if(j+1<len(grid[0])):
                        if(grid[i][j+1]<mi and grid[i][j+1]!=0):
                            mi=grid[i][j+1]
                    if(mi!=float('Inf')):
                        grid[i][j]=mi+1
        

        res=[]
        for i in grid:
            res.append(max(i)-1)
        return max(res)
