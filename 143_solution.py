"""
143. Sort Colors II
中文
English

Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
Example

Example1

Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]

Example2

Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]

Challenge

A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?
Notice

    You are not suppose to use the library's sort function for this problem.
    k <= n
"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        length = len(colors)
        
        for i in range(length):
            while colors[i] > 0:
                key = colors[i]-1
                if colors[key] < 0:
                    colors[key] -= 1
                    colors[i] = 0
                else:
                    colors[i] = colors[key]
                    colors[key] = -1

        index = length - 1
        for j in range(length-1, -1, -1):
            while colors[j] < 0:
                colors[index] = j+1
                index -= 1
                if index+1 == j:
                    break
                colors[j] += 1

if __name__ == "__main__":
    l = [3, 2, 2, 1, 4]
    l2 = [2, 1, 1, 2, 2]
    s = Solution()
    s.sortColors2(l, 4)
    s.sortColors2(l2, 2)
    print(l)
    print(l2)
