class Solution:
    def canJump(self, nums) -> bool:
        goal = [len(nums) - 1]
        for idx in range(len(nums) - 1, -1 , -1):
            if idx + nums[idx] >= goal[0]:
                goal[0] = idx
        return goal[0] == 0
        
solution = Solution()
print(solution.canJump([1,2,3,4,5,6,1,123,12,3123,1,23,0,11]))
