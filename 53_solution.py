class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        l = s.split(" ")
        res = ""
        for i in range(len(l)-1, 0, -1):
            if (l[i]):
                res += l[i] + " "
        if (l[0]):
            res += l[i]
        return res

if (__name__ == "__main__"):
    s = Solution()
    print (s.reverseWords("Hi   my     name   is   Conner   "))
    assert(s.reverseWords("Hi my name is Conner") == "Conner is name my Hi")
    assert(s.reverseWords("Hi") == "Hi")
    assert(s.reverseWords("") == "")

