class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res_stack = []
        future_counts = Counter(s)  # Count number of occurrences of each char in s
        used = defaultdict(bool)  # Find if specific char is already pushed onto stack
        for ch in s:
            # if used => decrement to get occurences in the remaining subsequence
            if used[ch]: 
                future_counts[ch] -= 1
                continue
            # if current char is less that the one on top, check if top appears in the remaining subsequence
            while res_stack and ch < res_stack[-1] and future_counts[res_stack[-1]] > 0:
                used[res_stack[-1]] = False
                res_stack.pop()
            # set used True
            used[ch] = True
            # decrement to get occurences in the remaining subsequence
            future_counts[ch] -= 1
            res_stack.append(ch)
        return ''.join(res_stack)
                        
                
        
        
