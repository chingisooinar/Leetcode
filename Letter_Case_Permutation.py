class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        newString = ""
        Q = [newString]
        while Q:
            newString = Q.pop(0)
            if len(newString) == len(s):
                res.append(newString)
                continue
            else:
                idx = len(s) - (len(s) - len(newString))
                ch = s[idx]
            if ch.isalpha():
                Upper = newString + ch.upper()
                Lower = newString + ch.lower()

                Q.append(Upper)
                Q.append(Lower)
            else:
                Q.append(newString + ch)
        return res
