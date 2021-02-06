class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        grey = []
        black = []
        for i in range(numCourses):
            courses[i] = []
            grey.append(0)
            black.append(0)
        for pair in prerequisites:
            a, b = pair
            courses[a].append(b)
        imp = [0]
        def dfs_visit(vertex):
            if imp[0] == 1:
                return
            grey[vertex] = 1
            for v in courses[vertex]:
                if grey[v] == 0 and black[v] == 0:
                    dfs_visit(v)
                elif grey[v] == 1:
                    imp[0] = 1
                    return
            black[vertex] = 1
            grey[vertex] = 0
            

        for i in range(numCourses):
            if black[i] == 0:
                dfs_visit(i)
            if imp[0]:
                return False

        return True
