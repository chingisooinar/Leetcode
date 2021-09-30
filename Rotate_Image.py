import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_dup = copy.deepcopy(matrix)
        
        n = len(matrix)
        
        for i in range(n - 1, -1, -1):
            vector = matrix_dup[i]
            for j in range(n):
                matrix[j][n - 1 - i] = vector[j]  
        
