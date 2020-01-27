class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[-1]
        i=0
        le=0
        maxi=0
        while(i!=len(s)):
            if(s[i]=='('):
                stack.append(i)
            elif len(stack)!=0 and s[i]==')':
                stack.pop()
                if(len(stack)==0):
                    stack.append(i)
                else:
                    maxi=max(maxi,i-stack[len(stack)-1])
            i+=1
        print(maxi)
        return maxi
