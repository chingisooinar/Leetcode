class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts.keys():
                counts[num] = 0
            counts[num] += 1
        res = sorted(counts.items(), key=lambda x:x[1], reverse=True)[:k]
        
        return [i for i, _ in res]
        
