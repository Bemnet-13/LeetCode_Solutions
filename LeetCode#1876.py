class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 3
        sub_str = s[l:r]
        good_sub = 0
        while r <= len(s):
            if sub_str[0] != sub_str[1] and sub_str[1] != sub_str[2] and sub_str[0] != sub_str[2]: 
                good_sub += 1
            l += 1
            r += 1
            sub_str = s[l:r]
        return good_sub