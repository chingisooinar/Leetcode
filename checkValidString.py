class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Recursion
        def dp(i, open_):
            if i == len(s):
                return open_ == 0
            if s[i] == '*':
                remove = False
                if open_ > 0:
                    remove = dp(i + 1, open_ - 1)
                return  remove or dp(i + 1, open_) or dp(i + 1, open_ + 1)
            elif s[i] == '(':
                return dp(i + 1, open_ + 1)
            elif s[i] == ')' and open_ > 0:
                return dp(i + 1, open_ - 1)
            return False
            
        return dp(0, 0)
        '''
        n = len(s)
        # worst case: there len(s) of '(' 
        dp = [[False for _ in range(n + 1)] for i in range(n + 1)]
        # base case
        dp[n][0] = True
        for i in range(n - 1, -1, -1):
            for open_ in range(n):
                ch = s[i]
                if ch == '*':
                    remove = False
                    # check if we can remove
                    if open_ > 0:
                        remove = dp[i+1][open_ - 1]
                    dp[i][open_] = remove or dp[i+1][open_] or dp[i+1][open_+1]
                elif ch == '(':
                    dp[i][open_] = dp[i+1][open_ + 1]
                # check if we can remove
                elif ch == ')' and open_ > 0:
                    dp[i][open_] = dp[i+1][open_ - 1]
        return dp[0][0]
            
