"""
133. Longest Word
中文
English

Given a dictionary, find all of the longest words in the dictionary.
Example

Example 1:
	Input: {
		"dog",
		"google",
		"facebook",
		"internationalization",
		"blabla"
		}
	Output: ["internationalization"]


Example 2:
	Input:  {
		"like",
		"love",
		"hate",
		"yes"		
		}
	Output: ["like", "love", "hate"]
"""

class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        res = []
        max_len = 0
        for i in range(len(dictionary)):
            if len(dictionary[i]) > max_len:
                res = []
                res.append(dictionary[i])
                max_len = len(dictionary[i])
            elif len(dictionary[i]) == max_len:
                res.append(dictionary[i])

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.longestWords(["a"]))
    print(s.longestWords(["a", "b", "c"]))
    print(s.longestWords(["a", "bb", "c"]))
    print(s.longestWords(["aa", "b", "c"]))
    print(s.longestWords(["a", "b", "cc"]))
    print(s.longestWords(["a", "b", "cc"]))
    print(s.longestWords(["aa", "b", "cc"]))
