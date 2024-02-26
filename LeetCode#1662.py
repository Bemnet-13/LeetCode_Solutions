class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        return "".join(self.word1) == "".join(self.word2)
    
trial = Solution()
print(trial.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))


        
        