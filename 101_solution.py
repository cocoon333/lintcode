class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if (not(nums)):
            return 0
        i = 0
        while (i < len(nums) - 2):
            prev = nums[i+1]
            pprev = nums[i]
            if (nums[i+2] == prev and nums[i+2] == pprev):
                nums.pop(i+2)
            else:
                i += 1
        return nums

if (__name__ == "__main__"):
    s = Solution()
    assert(s.removeDuplicates([-15,-7,-6,-1,1,2,6,11,15,15]) == [-15, -7, -6, -1, 1, 2, 6, 11, 15, 15])
    assert(s.removeDuplicates([-15,-7,-6,-1,1,1,1,2,6,11,15]) == [-15, -7, -6, -1, 1, 1, 2, 6, 11, 15])
    assert(s.removeDuplicates([-15,-7,-6,-1,1,1,1,2,6,11,15, 15, 15]) == [-15, -7, -6, -1, 1, 1, 2, 6, 11, 15, 15])
    assert(s.removeDuplicates([-14,-14,-13,-13,-13]) == [-14, -14, -13, -13])
    print(s.removeDuplicates([-8,0,1,2,3]))
