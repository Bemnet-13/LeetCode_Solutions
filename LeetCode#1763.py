class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Intuition
        # Find the set of all appearances of the letters used in the string
        # Use sliding window to 
        # If the current letter is found both in capital and small letters, then
        # Increase the window size by 1
        # If it is not, then slice the string upto the that character and if th esubstring is 
        # nice then store its length in  MAX_LEN VARIABLE

        # characters = set(s)

        start = 0
        end = 0
        max_len = ''

        while end < len(s):
            small = chr(ord(s[end]) + 32)
            cap = chr(ord(s[end]) - 32)
            possible_nice = set(s[start:])
            if small in possible_nice or cap in possible_nice:
                if end == len(s) - 1:
                    pos_nice = s[start:end + 1]
                    if self.isNice(pos_nice):
                        if len(pos_nice) > len(max_len):
                            max_len = pos_nice
                end += 1
            else:
                pos_nice = s[start:end]
                if self.isNice(pos_nice):
                    if len(pos_nice) > len(max_len):
                            max_len = pos_nice
                start = end + 1
                end += 1

        return max_len
    
    def isNice(self, s):
        characters = set(s)
        for char in characters:
            small = chr(ord(char) + 32)
            cap = chr(ord(char) - 32)

            if not (small in characters or cap in characters):
                return False
        return True

trial =Solution()
o = trial.longestNiceSubstring(s = "YazaAay")
print(o)
            