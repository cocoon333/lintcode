class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if (not(nums)):
            return 0
        previous = nums[0]
        i = 0
        while (i < len(nums) - 1):
            previous = nums[i]
            if (nums[i+1] == previous):
                nums.pop(i+1)
            else:
                i += 1
        return nums

if (__name__ == "__main__"):
    s = Solution()
    print(s.removeDuplicates([-15,-7,-6,-1,1,2,6,11,15,15]))
    print(s.removeDuplicates([-15,-7,-6,-1,1,1,2,6,11,15]))
    print(s.removeDuplicates([-14,-14,-13,-13,-13]))
    print(s.removeDuplicates([-14,-14,-13,-13,-13,-13,-13,-13,-13,-12,-12,-12,-12,-11,-10,-9,-9,-9,-8,-7,-5,-5,-5,-5,-4,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,14,14,14,14,15,16,16,16,18,18,18,19,19,19,19,20,20,20,21,21,21,21,21,21,22,22,22,22,22,23,23,24,25,25]))
