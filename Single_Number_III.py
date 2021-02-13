class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in nums:
            if i in res:
                res.pop()
            else:
                res.append(i)
        return res
