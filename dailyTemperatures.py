class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(T))]
        stack.append([T[0], 0])
        for i in range(1, len(T)):
            if not stack or T[i] <= stack[-1][0]:
                stack.append([T[i], i])
            else:
                while stack and T[i] > stack[-1][0]:
                    val, idx = stack.pop()
                    ans[idx] = i - idx
                stack.append([T[i], i])
        return ans
            
        
        
