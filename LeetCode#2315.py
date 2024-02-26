class Solution:
    def countAsterisks(self, s):
        splitted = s.split('|')
        count = 0
        for i in range(0, len(splitted), 2):
            count += (splitted[i]).count('*')

        return count
    
trial = Solution()
print(trial.countAsterisks("l|*e*et|c**o|*de|"))
