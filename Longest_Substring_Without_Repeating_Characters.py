class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        back, res = 0,0
        for front in range (len(s)):
            if (s[front] in s[back:front]):
                back = back + s[back:front].index(s[front]) + 1
            else:
                res = max(front-back+1, res)
        return res
                
        
