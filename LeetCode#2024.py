# Answer v--1.0 
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # define maximum and count variables t be 0
        # run a for loop to iterate throiugh each element
        # define a pointer movl and movr
        # compare each succedding element with the previous one 
        # if it is equal then increment both vals by 1
        # if not decrease both vals by 1 and k by 1 ---until k evals to 0
        # if k == 0 then maximum = max(maximum, count)
        # Answer v--1.0 
        ops = k
        maximum = 0
        for i in range(len(answerKey)):
            answer = answerKey[i]
            movl = i
            movr = movl + 1
            while k >= 0 and movr < len(answerKey):
                if answerKey[movl] == answerKey[movr]:
                    movl = movr
                    movr += 1
                elif answerKey[movl] != answerKey[movr] and k > 0:
                    k -= 1
                    movl = movr
                    movr += 1
                elif answerKey[movl] != answerKey[movr] and k == 0:
                    break
            
            maximum = max(maximum, movr-i)
            k = ops
        
        return maximum


trial = Solution()
o = trial.maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1)
print(o)