class Solution:
    def countSubstrings(self, s: str) -> int:
        # Intuition
        # Slice the string by increasing the sequence
        # and iterating through the string
        # check if the string is equivalent to the reversed string
        # increment the count by 1 
        
        count = 0
        for i in range(1, len(s) + 1):

            for m in range(len(s) + 1 - i):
                sub = s[m:m + i]
                if sub == sub[::-1]:
                    count += 1
        
        return count
    

trial = Solution()
o = trial.countSubstrings( s = "bab")
print(o)