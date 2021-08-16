class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while (left < right):
            if s[left].isalnum() is False:
                left += 1
                continue
            if s[right].isalnum() is False:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
            
            
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))