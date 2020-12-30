class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        convert = {')':'(', '}':'{',']':'['}
        for i in s:
            if i not in convert.keys(): #check if it is opening parentheses
                stack.append(i)
            elif len(stack) and stack[-1] == convert[i]:  #if not, top should match the incoming
                stack.pop()
            else: 
                return False
        if not stack: #if stack is empty -> it is valid
            return True
        return False
