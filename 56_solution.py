class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if((target - num) in d):
                return [d[target - num], i]
            d[num] = i

if (__name__ == "__main__"):
    s = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2]
    nums3 = [5, 4, 3, 2, 1]
    nums4 = [5, 6, 4, 7, 3]
    ans1 = s.twoSum(nums1, 7)
    ans2 = s.twoSum(nums2, 3)
    ans3 = s.twoSum(nums3, 4)
    ans4 = s.twoSum(nums4, 13)
    assert(nums1[ans1[0]] + nums1[ans1[1]] == 7)
    assert(nums2[ans2[0]] + nums2[ans2[1]] == 3)
    assert(nums3[ans3[0]] + nums3[ans3[1]] == 4)
    assert(nums4[ans4[0]] + nums4[ans4[1]] == 13)
