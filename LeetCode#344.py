class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Iterate through the list and 
        # while i < j
        # swap the value at index i to the value at j
        
        i = 0
        j = len(s) -1
        while i < j:
            s[i] , s[j] = s[j], s[i]
            i += 1
            j -= 1



            "bbaabbb"
        