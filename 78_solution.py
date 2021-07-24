"""
78. Longest Common Prefix
中文
English

Given k strings, find the longest common prefix (LCP).
Example

Example 1:
	Input:  "ABCD", "ABEF", "ACEF"
	Output:  "A"
	

Example 2:
	Input: "ABCDEFG", "ABCEFG" and "ABCEFA"
	Output:  "ABC"
"""

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        res = ""
        temp = ""
        for i in range(len(min(strs, key=len))):
            temp = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != temp:
                    return res
            res += temp
        return res

    def otherSolution(self, strs):
        if not strs:
            return (" ")
        mins=min(strs)
        maxs=max(strs)
        pre=""
        for i in range(min(len(mins),len(maxs))):
            if(mins[i]==maxs[i]):
                pre=pre+mins[i]
            else:
                break
        return(pre)

if __name__ == "__main__":
    s = Solution()
    assert(s.longestCommonPrefix(["ABCD", "ABEF", "ACEF"]) == 'A')
    assert(s.longestCommonPrefix(["ABCDEFG", "ABCEFG", "ABCEFA"]) == "ABC")
    print(s.otherSolution(["ABC", "AZZ", "ABZZ"]))
