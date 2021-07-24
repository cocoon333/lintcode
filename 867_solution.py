"""
867. 4 Keys Keyboard
中文
English

Imagine you have a special keyboard with the following keys:

    Key 1: (A): Print one 'A' on screen.
    Key 2: (Ctrl-A): Select the whole screen.
    Key 3: (Ctrl-C): Copy selection to buffer.
    Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.
Example

Example 1:

Input: 3
Output: 3
Explanation: A, A, A

Example 2:

Input: 7
Output: 9
Explanation: A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Notice

    1 <= N <= 50
    Answers will be in the range of 32-bit signed integer.
"""

class Solution:
    """
    @param N: an integer
    @return: return an integer
    """
    def maxA(self, N):
        res = [0]*(N)
        for i in range(0, N):
            res[i] = i+1
            print('i', i, 'res', res)
            for j in range(2, i):
                res[i] = max(res[i], res[i-j]*(j-1))
                print('j', j, 'res', res)
        return res[-1]

if __name__ == "__main__":
    s = Solution()
#    print(";LSDG;LKJASGD;JLDAG", s.maxA(30))
#    print(";LSDG;LKJASGD;JLDAG", s.maxA(35))
#    print('JLA;SG', s.maxA(15))
    print('A;DSGHOIJLE', s.maxA(25))
#    assert(s.maxA(3) == 3)
#    print(s.maxA(10))
#    assert(s.maxA(7) == 9)
#    assert(s.maxA(9) == 16)
