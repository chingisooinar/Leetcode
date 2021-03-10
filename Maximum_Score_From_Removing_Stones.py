class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = [a,b,c]
        piles.sort()
        res = 0
        while piles[1]:
            res += 1
            piles[1] -= 1
            piles[2] -= 1
            piles.sort()
        return res
