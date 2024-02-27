from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Intuition
        # Intialize a window with size of three and use the counter object to count
        # the occurence of each letter of a, b ,c
        # Use a while loop with start and end variables set to 0 and k
        # If the string is valid then increment len(s) - k 
        # then after the string is found valid increase start by 1 the decrease the value from the counter and if it zero, delete it 
        length = len(s)
        start = 0
        k = 3
        end = k - 1
        appearances = Counter(s[:end])
        count = 0

        while start < len(s):
            # Add the current value of end to the counter
            # If it contains all letters , then count += ..., then 
            # then decrease counter[s[start]] by one 
            # increase the start and end by 1
            # the
            # If it does not then increase end by 1

            appearances[s[end]] += 1
            if appearances['a'] >= 1 and appearances['b'] >= 1 and appearances['c'] >= 1:
                count += length - end
                appearances[s[start]] -= 1
                appearances[s[end]] -= 1
                start += 1
                
            else:
                if end < len(s) - 1:
                    end += 1
                else:
                    start += 1

        return count

trial = Solution() 
o = trial.numberOfSubstrings( s = "abc")
print(o)