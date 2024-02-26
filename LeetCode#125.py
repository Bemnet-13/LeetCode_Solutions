class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""

        for chr in s:
            if chr.isalnum():
                t += chr.lower()
        
        return t == t[::-1]