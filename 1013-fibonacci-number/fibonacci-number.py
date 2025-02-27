class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(n - 1):
            temp = b
            b = a + b
            a = temp
        return b