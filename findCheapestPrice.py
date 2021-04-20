class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        routes = {}
        start = src
        finish = dst
        for sublist in flights:
            src, dst, price = sublist
            if src not in routes.keys():
                routes[src] = []
            routes[src].append((dst, price))

        count = K
        q = [(start, count, 0)]
        visited = {}
        visited[start] = 0
        while q:
            src, count, price = q.pop(0)
            if src not in routes.keys(): continue
            for route in routes[src]:
                dst, cost = route
                if finish in visited.keys() and price + cost >= visited[finish]:
                    continue
                if count != 0 or dst == finish:
                    if dst in visited.keys() and price+cost <  visited[dst] or dst not in visited.keys(): 
                        visited[dst] = price + cost
                    if dst != finish:q.append((dst, count - 1, price + cost))
        return visited[finish] if finish in visited.keys() else -1
            
            
        
