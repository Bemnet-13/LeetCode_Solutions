class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        excel = {}
        for i in range(26):
            excel[chr(65 + i)] = i + 1
        
        columnTitle = columnTitle[::-1]
        equivalent = 0
        for i in range(len(columnTitle)):
            charac = columnTitle[i]
            equivalent += (excel[charac]) * 26**i
        return equivalent


trial = Solution()
o = trial.titleToNumber("")
print(o)