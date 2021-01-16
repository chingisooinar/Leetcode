class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        memog = [0]*10
        memos = [0]*10
        bull = 0
        cow = 0
        for s, g in zip(secret,guess):
            if s == g:
                bull += 1
            else:
                memos[int(s)] += 1
                memog[int(g)] += 1
                
        for s,g in zip(memos,memog):
            if s>=1 and g>=1:
                cow += min(s,g)
        out = f'{bull}A{cow}B'
        return out
        
