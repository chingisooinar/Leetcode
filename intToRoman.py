class Solution:
    def intToRoman(self, num: int) -> str:
        nums = []
        d = 10
        while num!=0:
            n = num%d
            if n != 0:
                nums.append(n)
            num = num // d * d
            d *= 10
        res = ''
        syms = ['I','V','X','L','C','D','M']
        vals = [1,5,10,50,100,500,1000]
        while nums:
            n = nums.pop()
            i = 0
            while i < len(vals) and vals[i] <= n:
                i += 1
            i -= 1
            if vals[i] == n:
                res += syms[i]
            elif i + 1 < len(vals) and vals[i + 1] - n in [1, 10, 100]:
                res += syms[vals.index(vals[i + 1] - n)]
                res += syms[i + 1]
            else:
                while n > 0:
                    n -= vals[i]
                    res += syms[i]
                    if vals[i] > n:
                        i -= 1
        return res
                
            
            
        
        
