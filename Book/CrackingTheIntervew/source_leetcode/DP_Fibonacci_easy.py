class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0:
            return first
        if n == 1:
            return second
        third = 0
        for index in range(2, n + 1):
            third = first + second
            first = second
            second = third
        return third

solution = Solution()
for i in range(12):
    print(solution.fib(i))