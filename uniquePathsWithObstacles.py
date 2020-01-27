class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ans=[]
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        for i in range(n):
            ans.append([0]*m)
        for i in range(m):
            if obstacleGrid[0][i]==1:
                ans[0][i]=0
                continue
            if(i!=0):
                ans[0][i]=ans[0][i-1]
            else:
                ans[0][i]=1
                
        for i in range(n):
            if obstacleGrid[i][0]==1:
                ans[i][0]=0
                continue
            if(i!=0):
                ans[i][0]=ans[i-1][0]
            else:
                ans[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    ans[i][j]=0
                    continue
                ans[i][j]=ans[i-1][j]+ans[i][j-1]
        return ans[-1][-1]
