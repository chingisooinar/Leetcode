import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = [] 
        for i in points:
            euclidean = math.sqrt((0 - i[0])**2 + (0 - i[1])**2)
            dists.append([euclidean,i])
        dists.sort(key=lambda x: x[0], reverse = False)
        out = [dists[i][1] for i in range(K)]
        return out
