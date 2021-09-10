class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # if k = 1, then make a list out of every element
        if k == 1:
            return [[x + 1] for x in range(n)]
        # if k == n, then the entire list is a combination
        if n == k:
            return [[x + 1 for x in range(n)]]
        # otherwise solve:
        # combine(n-1, k) -> a list of combinations excluding n
        # a list of combinations including n is a list of combinations having (k-1) elements excluding n + n to each combination
        # [x + [n] for x in self.combine(n - 1, k - 1)] a list of combinations including n
        return [x + [n] for x in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
