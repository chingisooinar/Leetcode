class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        inter = ""
        opens = ['(' for _ in range(n)]
        closes = [')' for _ in range(n)]

        def if_legal(inter):
            stack = []
            for i in inter:
                if i == '(':
                    stack.append(i)
                elif stack.__len__() != 0:
                    stack.pop()
            return stack.__len__() == 0

        def solve(opens, closes, inter):
            if opens.__len__() == 0 and closes.__len__() == 0:
                if if_legal(inter):
                    result.append(inter)
                return 
            else:
                if closes.__len__() > 0 and closes[1:].__len__() >= opens.__len__():
                    inter_close = inter + closes[0]
                    solve(opens, closes[1:], inter_close)
    
                if opens.__len__() > 0:
                    inter_open = inter + opens[0]
                    solve(opens[1:], closes, inter_open)
                

        solve(opens, closes, inter)
        return result
