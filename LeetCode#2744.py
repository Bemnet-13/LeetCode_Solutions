class Solution:
    def maximumNumberOfStringPairs(self, words):
        count = 0
        for i in range(len(words)):
            word = words[i]
            words[i] = '*'
            if self.reverse(word) in words:
                count += 1
        
        return count

    def reverse(self, word):
       return word[-1] + word[0]
    
