def DFS(coord,marked,grid,leni,lenj):
    stack=[coord]
    while(stack):
        c=stack.pop()
        i=c[0]
        j=c[1]
        marked[i][j]=1
        for di in range(-1,2):
            for dj in range(-1,2):
                if(abs(di)!=abs(dj)):
                    if(di+i>=0 and di+i<leni and dj+j>=0 and dj+j<lenj):
                        if(grid[di+i][dj+j]=="1" and marked[di+i][dj+j]==0):
                            stack.append([di+i,dj+j])
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if(len(grid)==0):
            return 0
        leni=len(grid)
        lenj=len(grid[0])
        marked=[]
        count=0
        for i in range(leni):
            marked.append([0]*lenj)
        for i in range(leni):
            for j in range(lenj):
                if(grid[i][j]=="1" and marked[i][j]==0):
                    DFS([i,j],marked,grid,leni,lenj)
                    count+=1
        return count
