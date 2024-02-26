from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter(s[:0])
        longest = l = r = 0
        while r < len(s):
            c[s[r]] += 1
            if c[s[r]] == 1:
                r += 1
                if sum(c.values()) > longest: #If it is unique
                    longest += 1
            else: #If it is not unique(occ>=2)
                c[s[l]] -= 1
                del c[s[l]]
                l += 1
        return longest
trial = Solution()
o = trial.lengthOfLongestSubstring(s = "abcbad")
print(o)