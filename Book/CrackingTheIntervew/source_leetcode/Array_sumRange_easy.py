class Solution:
    def summaryRanges(self, nums : list) -> list:
        answer = []
        i = 0
        len_arr = len(nums)
        while i < len_arr:
            j = i
            while j + 1 < len_arr and nums[j] + 1 == nums[j + 1]:
                j += 1
            
            if i == j:
                answer.append(str(nums[i]))
            else:
                answer.append(str(nums[i]) + "->" + str(nums[j]))

            i = j + 1
        return answer

solution = Solution()
print(solution.summaryRanges([1,2,3,4,5,6,8,9,10,12,13]))