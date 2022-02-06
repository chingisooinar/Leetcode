class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Recursion
        def dp(start):
            if start == len(s):
                return 1
            if start > len(s) or s[start] == '0':
                return 0
            sum_ = 0
            for i in range(2):
                ch_int = int(s[start:start + i + 1])
                if ch_int >= 1 and ch_int < 27:
                    sum_ += dp(start + i + 1)
            return sum_
        res = dp(0)
        return res 
        '''
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        for start in range(n - 1, -1, -1):
            if s[start] == '0':
                continue
            sum_ = 0
            for i in range(2):
                if start + i + 1 < n + 1:
                    ch_int = int(s[start:start + i + 1])
                    if ch_int >= 1 and ch_int < 27:
                        sum_ += dp[start + i + 1]
            dp[start] = sum_
        return dp[0]
            
