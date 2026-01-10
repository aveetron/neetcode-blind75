class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove the spaces and special characters first
        s = s.replace(" ", "")
        s = "".join(c for c in s if c.isalnum())
        if s.lower() == "".join(reversed(s)).lower():
            return True
        
        return False
        