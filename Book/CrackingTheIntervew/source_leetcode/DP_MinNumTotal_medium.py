class Solution:
    def minimumTotal(self, triangle) -> int:
        height = len(triangle)
        for i in range(height):
            for j in range(len(triangle[i])):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    triangle[i][j] += triangle[i - 1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j -1])
        return min(triangle[height - 1])

s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))