class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k  == len(num):
            return "0"
        targetlen = len(num) - k
        sequence = []
        for i in range(len(num)):
            cur = num[i]
            while sequence and sequence[-1] > cur and len(sequence) - 1 + len(num) - i >= targetlen:
                sequence.pop()
            if len(sequence) < targetlen:
                sequence.append(cur)
        
        return str(int(''.join(sequence)))
