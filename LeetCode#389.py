from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)

        for key in count_t:
            if count_t[key] != count_s[key]:
                return key
    
trial = Solution()
o = trial.findTheDifference(s = "abcd", t = "abcde")
print(o)