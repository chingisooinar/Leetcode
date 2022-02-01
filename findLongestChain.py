class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x:x[1])
        max_prev =  -float('inf')
        c = 0
        for p in pairs:
            min_cur = p[0]
            if min_cur > max_prev:
                c += 1
                max_prev = p[1]
        return c
