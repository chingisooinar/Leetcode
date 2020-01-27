
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        track=[]
        leni=len(grid)
        lenj=len(grid[0])
        for i in range(leni):
            track.append([float("inf")]*lenj)
        track[0][0]=grid[0][0]
        for i in range(leni):
            for j in range(lenj):
                for x in range(-1,2):
                    for y in range(-1,2):
                        if i+x>=0 and i+x<leni and j+y>=0 and j+y<lenj and abs(x)!=abs(y):
                            if(track[i+x][j+y]>track[i][j]+grid[i+x][j+y]):
                                track[i+x][j+y]=track[i][j]+grid[i+x][j+y]
        return(track[-1][-1])
