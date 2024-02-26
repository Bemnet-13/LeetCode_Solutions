class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dictionary = {}
        for i in arr:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        # print(dictionary.values())
        lst = []
        for i in dictionary.values():
            if i in lst:
                return False
            lst.append(i)
        return True
        
trial = Solution()
o = trial.uniqueOccurrences(arr = [1,2,2,1,1,3])
print(o)
