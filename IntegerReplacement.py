def solve(n):
    if(n==1):
        return 0
    if(n%2==0):
        return solve(n/2)+1
    else:
        return min(solve(n-1),solve(n+1))+1
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return solve(n)
