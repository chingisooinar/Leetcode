class Solution:
    def numSplits(self, s: str) -> int:
        count = 0
        memo = ""
        string = list(s)
        left = {}
        right = {}
        for c in s:
            right[c] = 1 + right.get(c, 0)
        while string:
            letter = string.pop(0)
            left[letter] = 1 + left.get(letter, 0)
            right[letter] -= 1
            if right[letter] == 0:
                del right[letter]
            if len(left.keys()) == len(right.keys()):
                count += 1
   
        return count
        
