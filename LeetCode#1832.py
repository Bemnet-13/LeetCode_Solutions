class Solution:
    def checkIfPangram(self, sentence):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(len(alphabet)):
            j = len(alphabet) - 1
            if not (alphabet[i] in sentence and alphabet[j] in sentence):
                return False
        return True


trial = Solution()
print(trial.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
