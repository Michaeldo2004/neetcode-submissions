class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not r or r[-1][1] < interval[0]:
                r.append(interval)
            else:
                r[-1] = [min(r[-1][0], interval[0]),
                        max(r[-1][1], interval[1])]
        return r
        