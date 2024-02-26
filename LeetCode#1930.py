class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Intutition
        # Find all the characters that exist in s
        # Find the count of the each charatcters: remove them if they exist less than two times
        # Iterate through the set and slice the string by using the rfind and find 
        # Have the set of chaaraters that reside within the two poles
        # Count hte characters and increase count by that number
        
        characters = set(list(s))
        endpoints = set()
        for char in characters:
            if s.count(char) >= 2:
                endpoints.add(char)
        
        count = 0
        for char in endpoints:
            l = s.find(char)
            r = s.rfind(char)
            sub = set(list(s[l+1:r]))
            count += len(sub)
        return count

trial = Solution()
o = trial.countPalindromicSubsequence(s = "bbcbaba")
print(o)


