from collections import Counter
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        mat = []
        st = 0
        m = 0
        while m < len(s):
            if s[st] == s[m] and m == len(s)-1:
                freq = s[m], m + 1-st
                mat.append(list(freq))
                m += 1
            elif s[st] == s[m]:
                m += 1
            else:
                freq = s[st], m-st
                mat.append(list(freq))
                st = m
        # print(mat)
        mat.sort(key= lambda item:item[1])
        print(mat)
        
        i = 0
        while k >= 0 and i < len(s):
            item = mat[i]
            print(item)
            if item[1] <= k:
                k = k - item[1]
                item[1] = 0
                i += 1
            else:
                break

        string = ""
        for j in range(i,len(mat)):
            mat[i][1] = str(mat[i][1])
            string += "".join(mat[i])
        
        print(len(string))




trial = Solution()
trial.getLengthOfOptimalCompression(s = "aabbaac", k = 2)