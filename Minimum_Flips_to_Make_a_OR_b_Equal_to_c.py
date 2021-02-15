class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a | b == c:
            return 0
        count = 0
        abit = [int(i) for i in list(str(bin(a))[2:])]
        bbit = [int(i) for i in list(str(bin(b))[2:])]
        cbit = [int(i) for i in list(str(bin(c))[2:])]
        while len(abit) != 32 or len(bbit) != 32 or len(cbit) != 32:
            if len(abit) != 32:
                abit.insert(0,0)

            if len(bbit) != 32:
                bbit.insert(0,0)

            if len(cbit) != 32:
                cbit.insert(0,0)
        for i in range(32):
            if cbit[i] == 1:
                if abit[i] | bbit[i] == 0:
                    count += 1
            else:
                if abit[i] == 1:
                    count += 1
                if bbit[i] == 1:
                    count += 1
        return count
