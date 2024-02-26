class Solution:
    def reverseWords(self, s):
        self.s = s
        if self.isSentenceValid(self.s) and 1 <= len(self.s) <= 50000:
            new_words = self.s.split()
            num_words = len(new_words)
            chr_list = list(self.s)
            reversed_word = ""
            for i in range(len(chr_list) - 1, -1, -1):
                reversed_word += chr_list[i]
            reversed_list = [""] * num_words
            rev_word_list = reversed_word.split()
            for i in range(num_words):
                reversed_list[i] += rev_word_list[num_words - i - 1]
            final = " ".join(reversed_list)
            return final
    def isSentenceValid(self, s):
        self.s = s
        words = s.split()
        for word in words:
            if not word.isascii():
                return False
        return True
    


trial1 = Solution()
input = "Let's take LeetCode contest".strip()
output = trial1.reverseWords(input)
print(output)