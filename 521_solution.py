"""
521. Remove Duplicate Numbers in Array
中文
English

Given an array of integers, remove the duplicate numbers in it.

You should:

    Do it in place in the array.
    Move the unique numbers to the front of the array.
    Return the total number of the unique numbers.

Example

Example 1:

Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4

Explanation:

    Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
    Return the number of unique integers in nums => 4.
    Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Example 2:

Input:
nums = [1,2,3]
Output:
[1,2,3]
3

Challenge

    Do it in O(n) time complexity.
    Do it in O(nlogn) time without extra space.

Notice

You don't need to keep the original order of the integers.
"""
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        seen = set()
        count = 0
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] not in seen:
                seen.add(nums[i])
                i += 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
        return len(seen)

if __name__ == "__main__":
    s = Solution()
    l1 = [1,3,1,4,4,2]
    l2 = [1, 2, 3]
    assert(s.deduplication(l1) == 4)
    assert(s.deduplication(l2) == 3)
    assert(l1[:4] == [1,3,2,4])
    assert(l2 == [1,2,3])
