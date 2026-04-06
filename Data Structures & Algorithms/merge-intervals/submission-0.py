class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()

        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            while i < len(intervals) - 1 and intervals[i + 1][0] <= end:
                end = max(end, intervals[i + 1][1])
                i += 1

            ret.append([start, end])
            i += 1
        return ret
            