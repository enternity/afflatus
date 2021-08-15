class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # eg : s = "abc", t = "abcd"
        # 0    0    0   0
        # 0    0    0   0
        # 0    0    0   0
        # 0    0    0   0
        # 0    0    0   0
        # After build matrix
        # 0    0    0   0
        # 0    1    1   1
        # 0    1    2   1
        # 0    1    2   3
        # 0    1    2   3        
        # final result is [4][3]
        
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(t)][len(s)] == len(s)
            

s = "acd"
t = "abcd"
solution = Solution()
print(solution.isSubsequence(s,t))