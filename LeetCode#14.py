class Solution:
    def longestCommonPrefix(self, strs):
        # Using in-built function startswith
        # comparator = list(strs[0])
        # for k in range(1, len(comparator)):
        #     for i in range(1, len(strs)):
        #         if not strs[i].startswith("".join(comparator)):
        #             comparator.pop() 
        # return "".join(comparator)

        # Using Iteration
        comparator = strs[0]
        for k in range(1, len(comparator)):
            for i in range(1, len(strs)):
                if not strs[i].startswith(comparator):
                    comparator = comparator[:-1]
        
        return comparator

       
       
       
       
       
       
       
       
        # output = ""
        # first_word = strs[0]
        # for i in range(len(first_word)):
        #     letter = first_word[i]
        #     for k in range(1, len(strs)):
        #         if strs[k][i] != letter:
        #             output =  first_word[:i]
        #             return output
        #     i += 1
        
        # output =  first_word[:i]
        # return output 















trial = Solution()
o = trial.longestCommonPrefix(strs = ["flower","flow","flight"])
print(o)