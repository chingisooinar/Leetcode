class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def if_op(t):
            return t in ("*", "+", "/", "-")
        
        while tokens:
            t = tokens.pop(0)
            if if_op(t):
                n2 = stack.pop()
                n1 = stack.pop()
                e = int(eval(''.join([n1, t, n2])))
                stack.append(str(e))
            else:
                stack.append(t)
        return stack.pop()
                
        
