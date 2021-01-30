import math
class Solution:
    def countBits(self, num: int) -> List[int]:
        out = [0]*(num+1)
        for i in range(1,num+1):
            if int(math.log(i,2)) == math.log(i,2):
                out[i] = 1
            else:
                if i % 2 == 1:
                    out[i] = out[i-1] + 1
                else:
                    out[i] = out[int(i/2)]
        return out
        
