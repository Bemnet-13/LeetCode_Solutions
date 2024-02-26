class Solution:
    def maxScore(self, s: str) -> int:  
    #     if s.count("0") == len(s) or s.count("1") == len(s):
    #         return len(s) - 1  
    #     last_0 = s.rfind('0')
    #     first_1 = s.find('1')
    #     if last_0 == len(s) - 1:
    #         last_0 -= 1
    #     if first_1 == 0:
    #         first_1 += 1
    #     score_1 = self.scoreCounter(s[:last_0 + 1], s[last_0 + 1:])
    #     score_2 = self.scoreCounter(s[:first_1], s[first_1:])
    #     return max(score_1, score_2)
    # def scoreCounter(self, s1, s2):
    #     return sum([s1.count("0"), s2.count("1")])
        maximum = 0

        for i in range(1, len(s)):
            counted = s[:i].count("0") + s[i:].count("1")
            maximum = max(maximum, counted)
        return maximum


    
    
trial = Solution()
o = trial.maxScore(s = "011101")
print(o)
    

