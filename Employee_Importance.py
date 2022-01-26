"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        id2e = {}
        for e in employees:
            id2e[e.id] = e
        stack = [id]
        memo = defaultdict(int)
        while stack:
            i = stack.pop()
            res += id2e[i].importance
            for n in id2e[i].subordinates:
                if memo[n] == 0:
                    memo[n] = 1
                    stack.append(n)
        return res
            
        
