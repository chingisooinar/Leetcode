class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        Q = [(sr, sc)]
        memo = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        while Q:
            i, j = Q.pop(0)
            image[i][j] = newColor
            for ix in range(-1, 2):
                for jx in range(-1, 2):
                    if abs(ix) != abs(jx) and i + ix >= 0 and i + ix < len(image) and j + jx >= 0 and j + jx < len(image[0]):
                        if image[i + ix][j + jx] == oldColor and memo[i + ix][j + jx] == 0:
                            memo[i + ix][j + jx] = 1
                            Q.append((i + ix, j + jx))
        return image
        
        
