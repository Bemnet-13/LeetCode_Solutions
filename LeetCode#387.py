class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Intuition
        # Iterate through the string and return the index if letter.count(string) == 1

        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1