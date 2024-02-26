import itertools
class Solution:
    def numDecodings(self, s: str) -> int:
        # 5 // 2 = 2
        # 5 % 2 = 1

        # 122
        # 212
        # 221

        # 1112
        # 1121
        # 1211
        # 2111

        # 11111
        dict = {1:len(s) % 2, 2: len(s) //2}
        comb = len(s) //2 + len(s) % 2
        for 
