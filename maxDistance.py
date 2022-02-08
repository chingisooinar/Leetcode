class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Recursion:
        def dp(i):
            if i == len(nums1) or i == len(nums2):
                return 0
            max_  = 0 
            for j in range(i, len(nums2)):
                if nums2[j] - nums1[i] >= 0:
                    max_ = max(max_, j - i)
                
            return max(max_, dp(i + 1))
        return dp(0)
        DP:
        n = min(len(nums2), len(nums1))
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            max_ = 0
            for j in range(i, len(nums2)):
                if nums2[j] - nums1[i] >= 0:
                    max_ = max(max_, j - i)
            dp[i] = max(max_, dp[i+1])
        return dp[0]
        '''
        left = 0
        right = 0
        ans = 0 
        while left < len(nums1):
            # max dist between any i and j is when j = len(nums2)
            while right < len(nums2) and nums2[right] - nums1[left] >= 0:
                right += 1
            ans = max(ans, right - left - 1)
            left += 1
        return ans
