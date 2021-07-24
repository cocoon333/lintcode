class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItsel(self, nums):
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if (j == i):
                    continue
                temp *= nums[j]
            res.append(temp)
        return res

    def productExcludeItself(self, nums):
        p = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res

if (__name__ == "__main__"):
    s = Solution()
    assert(s.productExcludeItself([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
    assert(s.productExcludeItself([0, 1, 2, 3, 4, 5]) == [120, 0, 0, 0, 0, 0])
    assert(s.productExcludeItself([]) == [])
    assert(s.productExcludeItself([1]) == [1])
