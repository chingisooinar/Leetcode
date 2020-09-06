class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=('(',')')
        output=[0]*len(s)
        left=0
        right=1
        stack=[]
        while left!=len(s):
            if s[left] in p:
                if s[left]=='(':
                    stack.append(left)
                else:
                    if stack:
                        num=stack.pop()
                        output[num]=1
                        output[left]=1
            left+=1
        word=""
        for i in range(len(s)):
            if s[i] in p :
                if(output[i]==1) :word+=s[i]
            else:
                word+=s[i]
        return word
                
