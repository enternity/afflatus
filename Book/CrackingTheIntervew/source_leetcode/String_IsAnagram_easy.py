
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bow = dict()
        for char in s:
            if char not in bow:
                bow[char] = 1
            else:
                bow[char] += 1
        
        for char in t:
            if char not in bow:
                return False
            else:
                bow[char] -= 1
        for key in bow:
            if bow[key] != 0:
                return False
        return True

solution = Solution()
print(solution.isAnagram("anagram", "naagrma"))