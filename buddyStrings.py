class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        mismatch_count = 0
        mismatches = [[],[]]
        occurancies = defaultdict(int)
        duplicate = False
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatch_count += 1
                mismatches[0].append(s[i])
                mismatches[1].append(goal[i])
            if occurancies[s[i]] == 0:
                occurancies[s[i]] += 1
            else:
                duplicate = True
        return (mismatch_count == 2 and set(mismatches[0]) == set(mismatches[1])) or (s == goal and duplicate)
        
