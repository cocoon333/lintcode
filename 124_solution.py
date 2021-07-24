"""
124. Longest Consecutive Sequence
中文
English

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Example

Example 1

Input : [100, 4, 200, 1, 3, 2]
Output : 4
Explanation : The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:4

Clarification

Your algorithm should run in O(n) complexity. 
"""
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        num = sorted(set(num))
        max_count = 1
        count = 1
        for i in range(len(num)):
            if i + 1 < len(num) and num[i+1] - 1 == num[i]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        return max_count

if __name__ == "__main__":
    s = Solution()
    assert(s.longestConsecutive([1, 2, 0, 1]) == 3)
    assert(s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
