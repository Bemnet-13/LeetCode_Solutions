class Solution:
    def finalString(self, s: str) -> str:
        faulty_lst = []
        for chr in s:
            if chr == 'i':
                faulty_lst.reverse()
            else:
                faulty_lst.append(chr)

        return "".join(faulty_lst)
    
trial = Solution()