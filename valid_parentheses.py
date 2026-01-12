class Solution:
    def isValid(self, s: str) -> bool:
        checker = {
            "(": ")",
            ")": "(",
            "{": "}",
            "}": "{",
            "[": "]",
            "]": "[",
        }
        

s = Solution()
print(s.isValid("([{])"))