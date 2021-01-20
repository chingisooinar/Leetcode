
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                ones = 0
                for di in range(-1,2):
                    for dj in range(-1,2):
                        if di != 0 or dj != 0 and di != dj:
                            if i + di >=0 and i + di < len(board) and dj + j >= 0 and dj+ j < len(board[0]):
                                if board[di+i][dj+j] == 1 or board[di+i][dj+j] == -1:
                                    ones += 1
                if ones == 3 and board[i][j] == 0:
                    board[i][j] = 2
                
                if ones < 2 and board[i][j] == 1:
                    board[i][j] = -1
                
                if ones > 3 and board[i][j] == 1:
                    board[i][j] = -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
