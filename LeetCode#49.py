from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        # Intuition
        # Use counter object for each string 
        # Use a dictionary to : Each key is a counter object and values are the  
        # array of strings that each who have the same counter object
        # Iterate through the dictionary vaalues and append each array one by one

        lst_count = []
        for string in strs:
            c = Counter(string)
            val = [string]
            if c not in lst_count:
                lst_count.append(c)
            
            
        # print(Counter({'e': 1, 'a': 1, 't': 1}) == Counter({'t': 1, 'e': 1, 'a': 1}))
        
        # print(lst_count)
                
        mat = [[] for i in range(len(lst_count))]
        
        for string in strs:
            idx = lst_count.index(Counter(string))
            if mat[idx] == []:
                mat[idx] = [string]
            else:
                mat[idx].append(string)
        
        if mat == [[]]:
            return [['']]
        return mat

trial = Solution()
o = trial.groupAnagrams([""])
print(o)