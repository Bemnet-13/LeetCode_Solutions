class Solution:
    def sortTheStudents(self, score, k: int):
        score.sort(key = lambda item : item[k], reverse = True)
        return score

trial = Solution()
o = trial.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2)
print(o)