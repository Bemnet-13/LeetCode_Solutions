class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        words = [word.strip() for word in words]


        count = 0
        for word in words:
            if self.isvalid(word):
                count += 1
        return count
            
        
    def isvalid(self, word):
        punc_marks = {".","!",","}
        
        hyph_valid = False
        if "-".count(word) == 0 or ("-".count == 1 and "-".find(word) < len(word)-1):
                hyph_valid = True 
                      
        
        punc_valid = False

        if (word[-1] in punc_marks and (".".count(word) +",".count(word)+"!".count(word) == 1)) or ("." not in word and "," not in word and "!" not in word):
            punc_valid = True
        
        for letter in word:
            if letter.isdigit():
                 return False      

        return hyph_valid and punc_valid
        

trial = Solution()
print(trial.countValidWords(sentence="he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))