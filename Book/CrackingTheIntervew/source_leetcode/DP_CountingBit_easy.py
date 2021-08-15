class Solution:
    def countBits(self, n: int):
        # If index is odd number. value at index'th = binary[index - 1] + 1
        # Else index is even number. value at index'th = binary[index >> 1] (value = index / 2)
        binary = [0]
        for index in range(1, n + 1):
            if index & 1:
                binary.append(binary[index - 1] + 1)
            else:
                binary.append(binary[index >> 1])
        return binary

solution = Solution()
print(solution.countBits(12))