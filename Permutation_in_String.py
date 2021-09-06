class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = 0
        r = len(s1) - 1
        s1Counter = Counter(s1)
        window = Counter()
        for c in s2[:r + 1]:
            window[c] += 1
            
        while r < len(s2):
            if window == s1Counter:
                return True
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                window[s2[r]] += 1
            else:
                return False
        return False
                
                            
                
                
                
        
