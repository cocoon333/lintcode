from collections import Counter
class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, string):
        c = Counter(string)
        for v in c.values():
            if (v > 1):
                return False
        return True

