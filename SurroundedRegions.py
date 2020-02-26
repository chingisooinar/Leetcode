def bfs(cord,board,marked):
    stack=[cord]
    while(stack):
        cord=stack.pop(0)
        i=cord[0]
        j=cord[1]
        for di in range(-1,2):
            for dj in range(-1,2):
                if abs(di)!=abs(dj):
                    if(di+i>=0 and di+i<len(board) and dj+j >=0 and dj+j<len(board[0]) and board[di+i][dj+j]=='O' and marked[di+i][dj+j]!=1):
                        marked[di+i][dj+j]=1
                        stack.append([di+i,dj+j])
    
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if(len(board)==0):
            return []
        marked=[]
        for i in range(len(board)):
            marked.append([0]*len(board[0]))
        for i in range(len(board[0])):
            if(board[0][i]=='O'):
                marked[0][i]=1
                bfs([0,i],board,marked)
            if(board[len(board)-1][i]=='O'):
                marked[len(board)-1][i]=1
                bfs([len(board)-1,i],board,marked)
        for i in range(len(board)):
            if(board[i][0]=='O'):
                marked[i][0]=1
                bfs([i,0],board,marked)
            if(board[i][len(board[0])-1]=='O'):
                marked[i][len(board[0])-1]=1
                bfs([i,len(board[0])-1],board,marked)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(marked[i][j]==0):
                    board[i][j]='X'
            
