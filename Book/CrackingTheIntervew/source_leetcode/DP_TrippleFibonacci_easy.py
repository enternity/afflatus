class Solution:
    def tribonacci(self, n: int) -> int:
        n_3, n_2, n_1, result = 0, 1, 1, 0
        if n >= 3:
            for index in range(3, n + 1):
                result = n_3 + n_2 + n_1
                n_3 = n_2
                n_2 = n_1
                n_1 = result
            return result
        else:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            
solution = Solution()
print(solution.tribonacci(1221))