class Solution:
    def maxSumAfterPartitioning(self, A: List[int], k: int) -> int:
        if len(A) <= k:
            return max(A) * len(A)
        @functools.lru_cache(None)
        def helper(j, maxi, i):
            if j - i > k: return -1
            if j == len(A): return maxi * (j - i)
            return max(maxi * (j - i) + helper(j+1, A[j], j), helper(j+1, max(A[j], maxi), i))
        return helper(1, A[0], 0)
