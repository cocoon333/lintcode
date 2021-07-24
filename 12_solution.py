class MinStack:
    
    def __init__(self):
        self.stack = []
        self.m = 999999999

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)
        if (number < self.m):
            self.m = number

    """
    @return: An integer
    """
    def pop(self):
        n = self.stack.pop()
        if (n == self.m):
            m = 999999999
            for i in range(len(self.stack)):
                if (self.stack[i] < m):
                    m = self.stack[i]
            self.m = m   
        return n

    """
    @return: An integer
    """
    def min(self):
        return self.m

