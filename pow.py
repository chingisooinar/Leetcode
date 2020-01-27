class Solution:
    def myPow(self, x: float, y: int) -> float:
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(y == 0): return 1
        temp = self.myPow(x, int(y / 2))  
      
        if (y % 2 == 0): 
            return temp * temp 
        else: 
            if(y > 0): return x * temp * temp 
            else: return (temp * temp) / x 
