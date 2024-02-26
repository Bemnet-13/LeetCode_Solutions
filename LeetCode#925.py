 class Solution:
    def isLongPressedName(self, name, typed):
        # i = j = 0
        # mapped = []
        # while i < len(name) and j < len(typed) - 1:
            
        #     if name[i] != typed[j]:
        #        i += 1
        #        tup = i,j
        #        mapped.append(tup)
        #     else:
        #        tup = i,j
        #        mapped.append(tup)
        #        j += 1

        f = []
        g = []

        for i in range(len(name)):
            tup = name[i], 1
            f.append(tup)

        print(f)
        for j in range(len(typed)):
            tup = name[j], 1
            g.append(tup)




        
trial = Solution()
print(trial.isLongPressedName(name = "saeed", typed = "ssaaedd"))

               
