class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        
        ordered = []
        for item in dict:
            freq = dict[item]
            string = freq * item
            ordered.append(string)

        ordered.sort(key= lambda s :len(s), reverse=True)
        return "".join(ordered)

trial = Solution()
trial.frequencySort("aadddc")
