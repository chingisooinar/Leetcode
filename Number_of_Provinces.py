class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0 for _ in range(len(isConnected))]
        count = 0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                stack = [i]
                while stack:
                    ix = stack.pop()
                    visited[ix] = 1
                    for j in range(len(isConnected[ix])):
                        if isConnected[ix][j] == 1 and ix != j and visited[j] == 0:
                            stack.append(j)
                count += 1
        return count       
