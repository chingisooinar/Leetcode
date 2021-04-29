class Solution:
    def intToRoman(self, num: int) -> str:
        d = 10
        res = []
        syms = ['I','V','X','L','C','D','M']
        vals = [1,5,10,50,100,500,1000]
        while num!=0:
            n = num%d
            if n != 0:
                i = 0
                while i < len(vals) and vals[i] <= n:
                    i += 1
                i -= 1
                if vals[i] == n:
                    res.append(syms[i])
                elif i + 1 < len(vals) and vals[i + 1] - n in [1, 10, 100]:
                    res.append(syms[vals.index(vals[i + 1] - n)] +  syms[i + 1])
                else:
                    tmp=''
                    while n > 0:
                        n -= vals[i]
                        tmp += syms[i]
                        if vals[i] > n:
                            i -= 1
                    res.append(tmp)
            num = num // d * d
            d *= 10
        res.reverse()
        return ''.join(res)
                
            
            
        
        
