class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans=[]
        for i in range(n):
            ans.append([0]*m)
        for i in range(m):
            ans[0][i]=1
        for i in range(n):
            ans[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                ans[i][j]=ans[i-1][j]+ans[i][j-1]
        return ans[-1][-1]
