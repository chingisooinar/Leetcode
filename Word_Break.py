class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = [0]
        visited = []
        while queue:
            start = queue.pop(0)
            if start in visited:continue
            visited.append(start)
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    if end == len(s):
                        return True
                    else:
                        queue.append(end)
                        
        return False
        
