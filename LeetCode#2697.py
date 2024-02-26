class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        lst = ['*' ]* len(s)
        for i in range(len(s)):
            j = len(s) - i
            if s[i] == s[j]:
                lst[i] = s[i]
            elif s[i] < s[j]:
                lst[i] = s[i]
            else:
                lst[i] = s[j]

        return "".join(lst)
                