class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_occurance = defaultdict(int)
        res = 0
        left = 0
        maxcount = 0
        for right, right_c in enumerate(s):
            window_occurance[right_c] += 1
            # count of most frequent char within window
            maxcount = max(maxcount, window_occurance[right_c])
            # (right - left) + 1 -> window length
            # window length - maxcount = # of char to replace
            while ((right - left) + 1) - maxcount > k:
                window_occurance[s[left]] -= 1
                left += 1
                
            res = max(res, (right - left) + 1)
        return res
            
        
