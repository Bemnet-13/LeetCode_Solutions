class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = list(str(num))
        l = 0
        r = k
        sub_num = num_str[l:r]
        result = 0
        while r <= len(num_str):
            sub_ = "".join(sub_num)
            if int(sub_) != 0 and num % int(sub_) == 0:
                result += 1
            sub_num.append(r)
            sub_num.pop(l)
            l += 1
            r += 1
        return result
trial = Solution()
o = trial.divisorSubstrings( num = 430043, k = 2)
print(o)
