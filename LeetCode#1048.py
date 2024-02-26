class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key = lambda word:len(word))
    
    
trial = Solution()
trial.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])