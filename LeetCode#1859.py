class Solution:
    def sortSentence(self, s):
        s_words = s.split()
        total_length = len(s_words)
        new_list = list(range(total_length))
        #  To check the constraints
        if self.validSentence(s_words) and 2 <= len(s) <= 200:
            for word in s_words:
                i = int(word[-1])
                new_list[i-1] = word
        sorted = " ".join(new_list)
        sorted_sentence = ""
        for word in sorted:
            for char in word:
                if not char.isdigit():
                    sorted_sentence += char

        return sorted_sentence

    def validSentence(self, jumbled_sentence):
        """ Returns True if the input matches the constraints """
        for word in jumbled_sentence:
            if not (word.isalnum() and '0' not in word):
                return False
        return True


trial = Solution()
print(trial.sortSentence("Myself2 Me1 I4 and3"))
