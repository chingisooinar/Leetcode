class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return not (num % 10 == 0 and num != 0)
        
