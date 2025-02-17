# Using simple iteration

class Solution:
    def Fibonacci(self, n: int) -> int:
        fib = [0] * (n + 1)
        fib[0], fib[1] = 0, 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]
solution = Solution()
n = int(input())
res = solution.Fibonacci(n)
print(res)

# Using Recursion

class Solution:
    def Fibonacci1(self, n: int) -> int:
        if n <= 1:
            return n
        return self.Fibonacci1(n - 1) + self.Fibonacci1(n - 2)
solution = Solution()
n = int(input())
res = solution.Fibonacci1(n)
print(res)