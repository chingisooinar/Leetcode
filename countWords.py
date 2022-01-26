class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        occurancies = {}
        for w in words1:
            occurancies[w] = occurancies.get(w, 0) + 1
        for w in words2:
            if occurancies.get(w, 0) == 1:
                count += 1
                occurancies[w] -= 2
            elif occurancies.get(w, 0) == -1:
                count -= 1
                occurancies[w] -= 1
        return count
        
