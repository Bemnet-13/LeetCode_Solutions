from collections import Counter
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        # Intuition
        # Count the occurence of each letter in chars
        # iterate through the list and 
        # if the count of the character is grater than that of the chars
        # continue
        # else:
        # increment count by the length of the list

        freq = Counter(chars)
        
        count = 0
        
        for word in words:
            for i in range(len(word)):
                if word[i] not in chars or word.count(word[i])> freq[word[i]]:
                    break
                
                if i == len(word) - 1:
                    count += len(word)
        
        return count

trial = Solution()
o = trial.countCharacters(["aaa","bb","ccc"], "abc")
print(o)