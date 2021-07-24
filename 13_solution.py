class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if (target == ""):
            return 0
        i = 0
        while(i < len(source)):
            for j in range(len(target)):
                print("j is", j)
                if (i + j >= len(source)):
                    return -1
                if (target[j] != source [i+j]):
                    if (j == 0):
                        j += 1
                    i += j
                    print ("i is ", i)
                    break
                if (j == len(target)-1):
                    return i
        return -1

if (__name__ == "__main__"):
    s = Solution()
    print(s.strStr("tartarget", "tg"))
