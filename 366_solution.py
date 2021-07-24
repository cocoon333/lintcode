class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
	    return self._fib(n-1)[0]

    def _fib(self, n):
        if (n == 0):
            return (0, 1)
	    else:
		    a, b = self._fib(n // 2)
		    c = a * (b * 2 - a)
		    d = a * a + b * b
    		if (n % 2 == 0):
	    		return (c, d)
		    else:
			    return (d, c + d)
