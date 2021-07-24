"""
30. Insert Interval
中文
English

Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).
Example

Example 1:

Input:
(2, 5) into [(1,2), (5,9)]
Output:
[(1,9)]

Example 2:

Input:
(3, 4) into [(1,2), (5,9)]
Output:
[(1,2), (3,4), (5,9)]
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return str((self.start, self.end))

class Solution:
    def insert(self, intervals, newInterval):
        index = self.binarySearch(intervals, newInterval)
        intervals.insert(index, newInterval)
        done = True
        while done:
            if len(intervals) == 1:
                return intervals
            curr = intervals[index]
            done = False
            if 0 < index < len(intervals)-1:
                prev = intervals[index-1]
                next_i = intervals[index+1]
                if prev.end >= curr.start:
                    done = True
                    curr.start = min(prev.start, curr.start)
                    curr.end = max(prev.end, curr.end)
                    intervals.pop(index-1)
                    index -= 1
                if intervals[index+1].start <= intervals[index].end:
                    done = True
                    curr.start = min(next_i.start, curr.start)
                    curr.end = max(next_i.end, curr.end)
                    intervals.pop(index+1)
            elif index > 0 and intervals[index-1].end >= curr.start:
                done = True
                curr.start = min(intervals[index-1].start, curr.start)
                curr.end = max(intervals[index-1].end, curr.end)
                intervals.pop(index-1)
            elif index < len(intervals)-1 and intervals[index+1].start <= curr.end:
                done = True
                curr.start = min(intervals[index+1].start, curr.start)
                curr.end = max(intervals[index+1].end, curr.end)
                intervals.pop(index+1)
        return intervals


    def binarySearch(self, intervals, newInterval):
        start = 0
        end = len(intervals) - 1
        mid = (start + end) // 2
        if newInterval.start < intervals[start].start:
            return start
        if newInterval.start > intervals[end].start:
            return end+1
        while start < end - 1:
            if intervals[mid].start <= newInterval.start:
                start = mid
            else:
                end = mid
        return end

if __name__ == "__main__":
    s = Solution()
    i1 = Interval(1, 2)
    i2 = Interval(3, 4)
    i3 = Interval(5, 7)
    assert(s.binarySearch([i1, i2, i3], Interval(2, 2)) == 1)
    assert(s.binarySearch([i1, i2, i3], Interval(0, 2)) == 0)
    assert(s.binarySearch([i1, i2, i3], Interval(6, 2)) == 3)
    assert(s.binarySearch([i1, i2, i3], Interval(4, 2)) == 2)

    print(s.insert([Interval(1, 5)], Interval(2, 3)))
    print(s.insert([Interval(1, 5), Interval(6, 8)], Interval(0, 9)))
    print(s.insert([Interval(1, 5), Interval(5, 9)], Interval(2, 5)))
