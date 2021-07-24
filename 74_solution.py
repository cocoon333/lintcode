"""
74. First Bad Version
中文
English

The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.
Example

Given n = 5:

    isBadVersion(3) -> false
    isBadVersion(5) -> true
    isBadVersion(4) -> true

Here we are 100% sure that the 4th version is the first bad version.

Challenge

You should call isBadVersion as few as possible.
Notice

Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)
"""

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        s = 1
        e = n
        m = (s + e) // 2
        while s < e:
            print(s, 's')
            print(e, 'e')
            print(m, 'm')
            if self.isBadVersion(m):
                e = m
            else:
                s = m + 1
            m = s + (e - s) // 2

        return s

    def isBadVersion(self, n):
        if n >= 2:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.findFirstBadVersion(4))
