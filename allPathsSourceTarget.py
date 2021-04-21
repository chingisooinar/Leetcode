class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        stack = [(0, 0)]
        path = []
        length = 0
        while stack:
            node, length = stack.pop()
            if length > len(path) - 1:
                path.append(node)
            else:
                path[length] = node
            if node == len(graph) - 1:
                paths.append(path[:length+1])
                continue
            for n in graph[node]:
                stack.append((n, length+1))
        return paths
                
            
        
        
