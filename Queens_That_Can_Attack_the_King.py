class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        chess = [[0 for _ in range(8)] for _ in range(8)]
        for i,j in queens:
            chess[i][j] = 1
        res = []
        for j in range(king[1]+1,8):
            if chess[king[0]][j] == 1:
                res.append([king[0], j])
                break
        for j in range(king[1]-1,-1,-1):
            if chess[king[0]][j] == 1:
                res.append([king[0], j])
                break
        for i in range(king[0]+1,8):
            if chess[i][king[1]] == 1:
                res.append([i, king[1]])
                break
        for i in range(king[0] - 1,-1,-1):
            if chess[i][king[1]] == 1:
                res.append([i, king[1]])
                break
        i, j = king
        while i != 7 and j != 7:
            i += 1
            j += 1
            if chess[i][j] == 1:
                res.append([i, j])
                break
        i, j = king
        while i != 0 and j != 0:
            i -= 1
            j -= 1
            if chess[i][j] == 1:
                res.append([i, j])
                break
        i, j = king
        while i != 0 and j != 7:
            i -= 1
            j += 1
            if chess[i][j] == 1:
                res.append([i, j])
                break
                i, j = king
        while i != 7 and j != 0:
            i += 1
            j -= 1
            if chess[i][j] == 1:
                res.append([i, j])
                break
        return res
