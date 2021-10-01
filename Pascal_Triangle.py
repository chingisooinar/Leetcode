class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            elements = i + 1
            l = [1 for _ in range(elements)]
            for j in range(elements):
                if j != 0 and j != elements - 1:
                    l[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(l)
        return pascal
