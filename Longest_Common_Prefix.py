class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        memo={}
        if len(strs) == 0:
            return ""
        k = 0
        for i in strs:
            for j in range(1,len(i)+1): #window
                if k+j <= len(i):
                    key = i[k:k+j]
                    if not key in memo.keys():
                        memo[key] = 0
                    memo[key] += 1


        if memo.items():
            sort = sorted(memo.items(), key = lambda x:x[1])#sort by # occurences
            if sort[-1][1] >= len(strs):
                return sort[-1][0] #return max
        return ""
