"""
421. Simplify Path
中文
English

Given an absolute path for a file (Unix-style), simplify it.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

The result must always begin with /, and there must be only a single / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the result must be the shortest string representing the absolute path.
Example

Example 1:

Input: "/home/"
Output: "/home"

Example 2:

Input: "/a/./../../c/"
Output: "/c"
Explanation: "/" has no parent directory, so "/../" equals "/".

Notice

    Did you consider the case where path is "/../"?

    In this case, you should return "/".

    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".

    In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        l = path.split('/')
        res = ['/']
        for i , element in enumerate(l):
            if not element:
                continue
            while element[0] == '/':
                l[i] = l[i][1:]
            if element == ".":
                continue
            elif element == "..":
                if len(res) > 1:
                    res.pop()
            else:
                res.append(element + '/')
        if len(res) == 1:
            return res[0]
        return "".join(res)[:-1]

if __name__ == "__main__":
    s = Solution()
    assert(s.simplifyPath('/home/') == '/home')
    assert(s.simplifyPath('/.') == '/')
    assert(s.simplifyPath("/a/./../../c/") == '/c')
