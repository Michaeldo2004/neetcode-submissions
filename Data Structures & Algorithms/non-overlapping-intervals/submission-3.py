class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        r = 0
        lastEnd = -50001

        for interval in intervals:
            if interval[0] >= lastEnd:
                lastEnd = interval[1]
            else:
                r += 1
                lastEnd = min(interval[1], lastEnd)
        return r



        