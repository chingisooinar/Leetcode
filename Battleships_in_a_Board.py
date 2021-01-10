class Solution:
    def checkAround(self, board, i, j):
        for di, dj in [(0, -1), (-1, 0)]:
            if i+di < len(board) and i+di >= 0 and j+dj < len(board[0]) and j+dj >= 0:
                if board[i+di][j+dj] == 'X':
                    return i+di, j+dj
        return -1,-1
                    
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    di, dj = self.checkAround(board, i, j)
                    if (-1 not in [di,dj]):
                        continue
                    else:
                        count += 1
        return count - 1
        
