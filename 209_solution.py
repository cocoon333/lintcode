from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        c=Counter(s)
        for k in c.keys():
            if(c[k]==1):
                return k
