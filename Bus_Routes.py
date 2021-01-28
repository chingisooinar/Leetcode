class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stops = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                    stops[routes[i][j]].add(i)

        count = 1
        queue = collections.deque()
        queue.append(S)
        visited = []
        visitedstops = []
        level = 0

        while queue:
            l = len(queue)
            for _ in range(l):
                stop = queue.popleft()

                if T == stop:
                    return level


                for bus in stops[stop]:
                    for i in routes[bus]:
                        queue.append(i)
                    routes[bus] = []
            level+=1

        return -1
