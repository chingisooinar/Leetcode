class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        min_, max_ = newInterval
        res = []
        inserted = False

        for inter in intervals:
            if min_ > inter[1]:
                res.append(inter)
            elif inter[0] > max_:
                if not inserted:
                    res.append([min_, max_])
                    inserted = True
                res.append(inter)
                
            else:
                min_ = min(min_, inter[0])
                max_ = max(max_, inter[1])

        if not inserted:
            res.append([min_, max_])
        return res
