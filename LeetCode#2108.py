class Solution:
    def firstPalindrome(self, words) -> str:
        palindrome_lst = []
        for word in words:
            if self.isPalindrome(word):
                palindrome_lst.append(word)
        
        if palindrome_lst == []:
            return ""
        return palindrome_lst[0]
    def isPalindrome(self, word):
        low = 0
        high = len(word) - 1

        while low < high:
            if word[low] != word[high]:
                return False
            
            low += 1
            high -= 1

        return True
