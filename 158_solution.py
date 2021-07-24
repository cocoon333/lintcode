from collections import Counter
class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        if (len(s) != len(t)):
            return False
        sc = Counter(s)
        st = Counter(t)
        print(sc)
        print(st)
        sck = list(sc.keys())
        stk = list(st.keys())
        for i in range(len(sck)):
            if (not(sck[i] in st.keys())):
                return False
            elif(sc[sck[i]] != st[sck[i]]):
                return False
        return True

if (__name__ == "__main__"):
    s = Solution()
    print(s.anagram("az", "by"))
