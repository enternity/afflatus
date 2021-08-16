class Solution:
    def rob(self, nums: list) -> int:
        rob1, rob2 = 0, 0
        
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
        
s = Solution()
print(s.rob([2,1,1,2]))
        