def findmax(s,l,r):

    while(l>=0 and r<len(s) and s[l]==s[r]):
        l-=1
        r+=1
    word=s[l+1:r]
    return word
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxi=0
        res=""
        left=right=index=0
        for i in range(len(s)):
            word1=findmax(s,i,i)
            word2=findmax(s,i,i+1)
            opts=[[word1,len(word1)],[word2,len(word2)]]
            opts.sort(key=lambda x:x[1],reverse=True)
            word=opts[0][0]
            if len(word)>maxi:
                maxi=len(word)
                res=word
        return res
