class Solution:
    def mostWordsFound(self, sentences):
        self.sentences = sentences
        valid_sentence_list = []
        if 1 <= len(self.sentences) <= 100:
            for sentence in self.sentences:
                if 1 <= len(sentence) <= 100:
                    valid_sentence_list.append(sentence)

        total_words = []
        for sentence in valid_sentence_list:
            sentence_words = sentence.split()
            if self.noWhiteSpaces(sentence_words):
                total_words.append(len(sentence_words))
        max_word = max(total_words)
        return max_word

    def noWhiteSpaces(self, word_lst):
        self.word_lst = word_lst
        for word in self.word_lst:
            if not word.isalpha():
                return False
        return True


trial = Solution()
print(trial.mostWordsFound(["alice and bob love leetcode",
                            "i think so too", "this is great thanks very much"]))
