from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        _sliding = Counter(s2[:len(s1)])
        # Check conditions
        if len(s1) > len(s2): # It cannot possibly be a permutation
            return False
        if target == _sliding:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            # Window is sliding
            _sliding[s2[r]] += 1
            _sliding[s2[l]] -= 1
            if _sliding == target:
                return True
            r += 1
            l += 1
        return False

trial = Solution()
o = trial.checkInclusion(s1 = "ab", s2 = "eidboaoo")
print(o)