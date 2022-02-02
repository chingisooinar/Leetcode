class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                if  len(word) <= (i + 1) and s[i - len(word) + 1:i + 1] == word and dp[i - len(word) + 1]:
                    dp[i + 1] = True
                    break
        return dp[-1]
                
        
