class Solution:
    def replaceDigits(self, s):
        lst = ["*"] * len(s)
        print(len(s))
        for i in range(0, len(lst) - 1, 2):
            lst[i] = s[i]
            shifted = self.shift(s[i], int(s[i + 1]))
            lst[i+1] =  shifted

        if len(lst) % 2 != 0:
            lst[-1] = s[-1]
        return "".join(lst)

    def shift(self, c, x):
        ascii_code = ord(c) + x
        return chr(ascii_code)


trial = Solution()
output = trial.replaceDigits(s="a1c1e1")
print(output)
