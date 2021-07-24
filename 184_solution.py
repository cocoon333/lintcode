"""
184. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.
Example

Example 1:

Input:[1, 20, 23, 4, 8]
Output:"8423201"

Example 2:

Input:[4, 6, 65]
Output:"6654"

Challenge

Do it in O(nlogn) time complexity.
Notice

The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    def largestNumber(self, nums):
        res = ""
        l = self.helper(list(map(str, nums)))
        for s in l:
            res += s
        return str(int(res))

    def helper(self, nums):
        if len(nums) < 2:
            return nums
        mid = (len(nums)-1)//2
        return self.merge(self.helper(nums[:mid+1]), self.helper(nums[mid+1:]))

    def merge(self, n1, n2):
        if not n1:
            return n2
        elif not n2:
            return n1
        res = []
        i = 0
        j = 0
        while i < len(n1) and j < len(n2):
            char_i = n1[i]
            char_j = n2[j]
            broken = False
            op1 = char_i + char_j
            op2 = char_j + char_i
            if op1 >= op2:
                res.append(char_i)
                i += 1
                continue
            else:
                res.append(char_j)
                j += 1
                continue
        if i < len(n1):
            res.extend(n1[i:])
        else:
            res.extend(n2[j:])
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.largestNumber([0, 0]) == '0')
    assert(s.largestNumber([25,5,12,97,3,8,79,73,38,88,98,29,84,74,16,2,67,65,41,44,88,75,51,87,95,90,45,40,7,53,5,30,77,5,56,58,41,51,62,88,33,69,81,78,18,63,82,90,21,6,12,92,67,6,81,83,14,6,76,85,79,96,41,44,20,89,59,58,83,58,73,1,41,41,24,55,61,49,10,42,5,1,98,30,91,9,34,5,84,43,73,4,22,11,21,14,1,62,77,41]) == "998989796959291909089888888887858484838382818179797877777767574737373696767666656362626159585858565555555535151494544444434241414141414140383433330302925242222121201816141412121111110")
    assert(s.largestNumber([3577,9155,9352,7911,1622]) == "93529155791135771622")
    assert(s.largestNumber([1, 20, 23, 4, 8]) == '8423201')
    assert(s.largestNumber([4, 6, 65]) == "6654")
