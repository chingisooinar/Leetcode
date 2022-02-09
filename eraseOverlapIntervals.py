class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        count = 0
        prev_max = -float('inf')
        # Greedy approach:
        # longest array will be if we take short intervals as much as possible
        # Thus, min # arrays to drop is: initial length - length of longest non-overlapping array of intervals
        for interval in intervals:
            cur_min, cur_max = interval
            if prev_max <= cur_min:
                count += 1
                prev_max = cur_max
            else:
                prev_max = min(prev_max, cur_max)

        return len(intervals) - count
