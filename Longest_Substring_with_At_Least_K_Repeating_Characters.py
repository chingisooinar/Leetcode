class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 1 and k == 1:
            return 1
        counter = {}
        for i in s:
            if i not in counter.keys():
                counter[i] = 0
            counter[i] += 1
        valid = True
        start = 0
        maxlen = 0
        for end in range(len(s)):
            if counter[s[end]] < k:
                maxlen = max(maxlen, self.longestSubstring(s[start:end],k))
                start = end + 1
                valid = False
        if valid:
            return len(s)
        else:
            return max(maxlen, self.longestSubstring(s[start:],k))
