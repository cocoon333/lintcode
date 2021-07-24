"""
156. Merge Intervals
中文
English

Given a collection of intervals, merge all overlapping intervals.
Example

Example 1:

Input: [(1,3)]
Output: [(1,3)]

Example 2:

Input:  [(1,3),(2,6),(8,10),(15,18)]
Output: [(1,6),(8,10),(15,18)]

Challenge

O(n log n) time and O(1) extra space.
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        print(intervals)
        res = []
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                res.append(Interval(intervals[i].start, intervals[i+1].end))
            else:
                res.append(intervals[i])
        return res

if __name__ == "__main__":
    s = Solution()
    #print(s.merge([(1, 3), (2, 6), (8, 10), (15, 18)]))
    #print(s.merge([(1, 3)]))
    print(s.merge([Interval(1,4), Interval(0,2), Interval(3,5)]))
