class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Intuition
        # Use set to find all the characters that appear in s 
        # Iterate through the set and find the occurence of each letter in each and compare
        # return False if that's not the case


        chars =  set(list(s))

        if len(s) != len(t):
            return False
        
        for letter in chars:
            if s.count(letter) != t.count(letter):
                return False
        return True