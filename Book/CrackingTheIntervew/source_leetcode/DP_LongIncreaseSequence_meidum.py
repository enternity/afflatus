class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        for i in range(len(nums) - 1, -1, -1):
            max_val = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_val = max(max_val, 1 + dp[j])
            dp[i] = max_val

        return max(dp)

s = Solution()
print(s.lengthOfLIS([0,1,0,3,2,3]))