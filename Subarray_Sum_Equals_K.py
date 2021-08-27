class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_sums = defaultdict(int)
        map_sums[0] = 1
        sums = 0
        count = 0
        for num in nums:
            sums += num
            count += map_sums[sums - k]
            map_sums[sums] += 1
        return count
        
