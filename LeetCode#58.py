class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Intuition
        # trim the string
        # split the string by using a white space
        # return the last string in the list

        lst_words = s.split(" ")

        return len(lst_words[-1].trim())