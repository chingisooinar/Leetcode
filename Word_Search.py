class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ptr = 0
        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[ptr]:
                    ptr += 1
                    stack.append([i,j,ptr])
                    active = [(i,j)]
                    while stack:
                        x,y, ptr = stack.pop()
                        if ptr == len(active):
                            active.append((x,y))
                        else:
                            active[ptr] = (x,y)
                            active = active[:ptr+1]
                        if ptr == len(word):
                            return True
                        for dx in range(-1,2):
                            for dy in range(-1,2):
                                if abs(dx) != abs(dy):
                                    if dx + x >= 0 and dx + x < len(board) and dy + y >=0 and dy + y < len(board[0]):
                                        if board[dx+x][dy+y] == word[ptr] and (dx+x,dy+y) not in active:
                                            stack.append([dx+x,dy+y,ptr+1])
                    ptr = 0
        
