class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        memo = defaultdict(int)
        for num in target:
            memo[num] += 1
        for num in arr:
            memo[num] -= 1
        for val in memo.values():
            if val != 0:
                return False
        
        return True
          
