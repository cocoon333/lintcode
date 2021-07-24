"""
644. Strobogrammatic Number
中文
English

A mirror number is a number that looks the same when rotated 180 degrees (looked at upside down).For example, the numbers "69", "88", and "818" are all mirror numbers.

Write a function to determine if a number is mirror. The number is represented as a string.
Example

Example 1:

Input : "69"
Output : true

Example 2:

Input : "68"
Output : false
"""

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        reversable_nums = {'1':'1', '8':'8', '6':'9', '9':'6', '0':'0'}
        reverse = ""
        for i in range(len(num)-1, -1, -1):
            if num[i] in reversable_nums:
                reverse += reversable_nums[num[i]]
        return reverse == num

if __name__ == "__main__":
    s = Solution()
    assert(s.isStrobogrammatic("69"))
    assert(s.isStrobogrammatic("0"))
    assert(not s.isStrobogrammatic("68"))
