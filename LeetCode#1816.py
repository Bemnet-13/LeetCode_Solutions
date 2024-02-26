class Solution:
    def truncateSentence(self, s, k):
        self.s = s
        self.k = k
        sentence_words = self.s.split()
        no_of_words = len(sentence_words)
        valid = False
        if self.isSentenceValid(sentence_words, no_of_words, self.k) and 1 <= len(s) <= 500:
            valid = True

        if valid:
            truncated = self.sentence_words[:k]
            truncated_sentence = " ".join(truncated)
            return truncated_sentence

    def isSentenceValid(self, sentence_words, no_words, k):
        self.sentence_words = sentence_words
        self.no_words = no_words
        for word in self.sentence_words:
            if not (1 <= k <= self.no_words and word.isalpha()):
                return False
        return True


# Test Program

test1 = Solution()
user_input = "What is the solution to this problem".strip()
output = test1.truncateSentence(user_input, 4)
print(output)
