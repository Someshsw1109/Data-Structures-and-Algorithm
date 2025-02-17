# Check if a given string is palindrome or not....

# If palindrome function should return True or otherwise it returns False

class Solution:
    def IsPalindromeOrNot(self, i: int, s: str) -> bool:
        n = len(s)
        if i >= n // 2:
            return True
        if s[i] != s[n - i - 1]:
            return False
        return self.IsPalindromeOrNot(i + 1, s)

solution = Solution()
i = 0
s = input()
res = solution.IsPalindromeOrNot(i, s)
print(res)
