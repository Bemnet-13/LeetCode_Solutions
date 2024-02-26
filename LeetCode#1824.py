class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Intuition
        # reverse the string s and store it in another variable
        # Initialize a maximum variable
        # Iterate through the string using the index and find the index in the reverse string
        #  i = k
        #  j = m
        #  sub = (len(s) - 1 - m) - k
        # Use max function to maximum = max(maximum, sub)
        # return maximum

        t = s[::-1]
        
        maximum = -1
        
        for i in range(len(s)):
            j = t.find(s[i])
            sub = ((len(s) - 1 - j) - i ) - 1
            maximum = max(maximum, sub)
        return maximum


trial = Solution()
o = trial.maxLengthBetweenEqualCharacters(s = "abcaa")
print(o)