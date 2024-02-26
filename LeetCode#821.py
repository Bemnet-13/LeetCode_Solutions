class Solution:
    def shortestToChar(self, s: str, c: str):
        lst = []
        for i in range(len(s)):
            if s[i] == c:
                lst.append(i)
        
        res = []
        j = 0
        for i in range(len(s)):
            if i < lst[j]:
                res.append(lst[j] - i)
            elif s[i] == c:
                res.append(0)
            else:
                j += 1
                if j + 1 < len(lst):
                    ls = abs(lst[j] - i), abs(lst[j-1] - i), abs(lst[j+1] -1)
                    res.append(min(ls))
                else:
                    ls = abs(lst[j] - i), abs(lst[j-1] - i)
                    res.append(min(ls))

trial = Solution()
trial.shortestToChar(s = "loveleetcode", c = "e")
     