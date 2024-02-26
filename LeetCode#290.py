class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = s.split(" ")
        # pattern = list(pattern)
        # mapped = list(zip(pattern, s))
        # def sorter(item):
        #     return ord(item[0])
        
        # mapped.sort(key = sorter)
        # i = 0
        # j = 1

        # while j < len(mapped):
        #     if mapped[i][0] == mapped[j][0] and mapped[i][1] != mapped[j][1]:
        #         return False
        #     if mapped[i][0] != mapped[j][0] and mapped[i][1] == mapped[j][1]:
        #         return False
        #     i += 1
        #     j += 1
        #     return True
        
        
        
        # split s into words
        splited = s.split(" ")
        mapped = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            if mapped.get(letter) == None:
                mapped[letter] = splited[i]
            else:
                if mapped.get(letter) != splited[i]:
                    return False
        
        for word in mapped.values():
            if (mapped.values()).count(word) != 1:
                return False
        return True

    
trial = Solution()
print(trial.wordPattern(pattern = "abba", s = "dog cat cat dog"))
