'''
56. Merge Intervals


'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if [] == intervals:
            return []

        intervals = sorted(intervals, key = lambda interval:interval.start)
        l_intervals = len(intervals)
        indexes = [0]

        if 1 == l_intervals:
            return intervals
        for i in range(1, l_intervals):
            if intervals[i].start <= intervals[i-1].end:
                intervals[i].start = intervals[i-1].start
                if intervals[i].end < intervals[i-1].end:
                    intervals[i].end = intervals[i-1].end

                indexes[-1] = i
            else:
                indexes.append(i)
        return [intervals[i] for i in indexes]


name = [[1,4],[4,6],[8,10],[15,18]]
prob = []
for i in name:
    prob.append(Interval(i[0],i[1]))

c = Solution()
d = c.merge(prob)
print(d)


