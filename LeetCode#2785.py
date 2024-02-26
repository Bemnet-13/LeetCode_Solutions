class Solution:
    def sortVowels(self, s: str) -> str:
        t = []
        vowels_lst = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        vowels = []
        for chr in s:
            if chr in vowels_lst:
                t.append("*")
                vowels.append(chr)
            else:
                t.append(chr)

        vowels.sort(key=lambda chr: ord(chr))

        i = 0
        for j in range(len(t)):
            if t[j] == "*":  
                t[j] = vowels[i]
                i += 1
        
        return "".join(t)

trial = Solution()
o = trial.sortVowels(s = "lEetcOde")
print(o)

