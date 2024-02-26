class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Intuition
        # Iterate through the loop one character at a time
        # Store k on res 
        # If the s[i] == curr, then i += 1
        # Else decrease k by one 
        # if k = -1 store the count by decreasing current index i and j
        res = k
        maximum = 0
        for i in range(len(s)):
            k = res
            for j in range(i + 1, len(s)):
                if s[i] != s[j]:
                    k -= 1
                if s[i] == s[j] and j != len(s) - 1:
                    continue
                elif s[i] == s[j] and j == len(s) - 1:
                    maximum = max(maximum, j - i)
                    break
                if k == -1 or j == len(s) - 1:
                    maximum = max(maximum, j - i)
                    break
            # if maximum > len(s) - i:
            #     break
        return maximum
    
trial =Solution()
o = trial.characterReplacement(s = "AABABBA", k = 1)
print(o)






# trial = Solution()
# o = trial.characterReplacement(s = "CABAAA", k = 1)
# print(o)






# appearance = {}
        # app = 0
        # most_app_chr = ''
        # for letter in s:
        #     appearance[letter] = s.count(letter)
        #     if s.count(letter) > app:
        #         app = s.count(letter)
        #         most_app_chr = letter
        
        # print("most app", most_app_chr, "app", app)
        
        # splited = list(s)
        # print("before modifying", splited)
        # for i in range(len(splited)):
        #     if splited[i] != most_app_chr and k >0:
        #         splited[i] = most_app_chr
        #         k -= 1
        
        # # Counting the longest character repetition
        # i = 1
        # max_len = 0
        # count = 1
        # while i < len(splited):
        #     if splited[i] == splited[i-1]:
        #         count += 1
        #     else:
        #         count = 1
        #     i += 1
            
        #     max_len = max(max_len, count)

        # # In case the length of s is 1
        # max_len = max(max_len, count)
        # return max_len
