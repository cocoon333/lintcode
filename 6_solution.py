class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        j = 0
        k = 0
        res = []
        for i in range(len(A) + len(B)):
            if(A[j] < B[k]):
                print (j)
                res.append(A[j])
                j += 1
            else:
                print(k)
                res.append(B[k])
                k += 1
            if (j==len(A)):
                res.extend(B[k:])
                break
            if (k == len(B)):
                res.extend(A[j:])
                break
        return res

if (__name__ == "__main__"):
    s = Solution()
    s.mergeSortedArray([7], [5, 7])
