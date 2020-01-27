class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        stack=[]
        for i in strs:
            a=list(i)
            a.sort()
            if a not in stack:
                stack.append(a)
                res.append([i])
            else:
                for j in range(len(stack)):
                    if(a==stack[j]):
                        res[j].append(i)
                
        return res
