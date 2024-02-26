class Solution:
    def makeEqual(self, words) -> bool:
        # Intuition
        # Join the array to  form one whole string
        # We can count the occurence of each letter across the whole array of strings
        # If occ % len(arr) == 0, then return True
        # else False

        s = "".join(words)

        freq = {}

        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for occurence in freq.values():
            if occurence % len(words) != 0:
                return False
        return True

