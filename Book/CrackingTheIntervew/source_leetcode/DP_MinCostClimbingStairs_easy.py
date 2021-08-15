class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n_1, n_2, n = 0, 0, 0
        for index in range(2, len(cost) + 1):
            n = min(cost[index - 1] + n_1, cost[index - 2] + n_2)
            n_2 = n_1
            n_1 = n
        return n
        


solution = Solution()
print(solution.minCostClimbingStairs([10,15,20,1]))