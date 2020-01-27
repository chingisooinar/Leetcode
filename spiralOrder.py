class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(len(matrix)==0):
            return []
        lend=len(matrix[0])
        lens= len(matrix)
        marked=[]
        for i in range(lens):
            marked.append([0]*lend)
        res=[matrix[0][0]]
        i=0
        j=0
        marked[0][0]=1
        right=0
        down=1
        left=2
        up=3
        direction=right
        count=0
        while(1):
            if(count==4):
                break
            if(direction==right):
                if(j+1<lend and marked[i][j+1]!=1):
                    j+=1
                else:
                    direction=(direction+1)%4
                    count+=1
                    continue
            elif(direction==down):
                if(i+1<lens and marked[i+1][j]!=1):
                    i+=1
                else:
                    direction=(direction+1)%4
                    count+=1
                    continue
            elif(direction==left):
                if(j-1>=0 and marked[i][j-1]!=1):
                    j-=1
                else:
                    direction=(direction+1)%4
                    count+=1
                    continue
            elif(direction==up):
                if(i-1>=0 and marked[i-1][j]!=1):
                    i-=1
                else:
                    direction=(direction+1)%4
                    count+=1
                    continue
            count=0
            marked[i][j]=1
            res.append(matrix[i][j])

            
 
        return res
