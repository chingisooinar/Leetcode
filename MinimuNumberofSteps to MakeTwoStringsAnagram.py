class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s=list(s)
        t=list(t)
        t.sort()
        s.sort()
        if(t==s):
            return 0
        count=0
        ds={}
        for i in range(len(s)):
            if(s[i] not in ds.keys()):
                ds[s[i]]=1
            else:
                ds[s[i]]+=1
        for i in t:
            if(i in ds.keys()):
                ds[i]-=1
        for i in ds.values():
            if(i>0):
                count+=i
        return count
