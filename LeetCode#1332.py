class Solution:
    def removePalindromeSub(self, s: str) -> int:
        k = list(s)
        if k == k[::-1]:
            return 1
        return 2
     