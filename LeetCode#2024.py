class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Intuition
        # Define a function that takes in  the answerKey, the opposing answer,
        # the coverted answer and k
        # return the maximum of the two situation

        return max(self.maxConsectutiveWith(answerKey, k, 'T', 'F'), self.maxConsectutiveWith(answerKey, k, 'F', 'T'))
    
    def maxConsectutiveWith(self, answerKey, k, corr, opp):
        start = end = max_len = 0

        while end < len(answerKey):
            if k < 0:
                start += 1
                if answerKey[start - 1] == opp:
                    k += 1 
            elif end == len(answerKey) - 1:
                if answerKey[end] == opp:
                    k -= 1
                if k < 0:
                    max_len = max(max_len, end - start)
                    break
                else:
                    max_len = max(max_len, end - start + 1)
                    break
            elif answerKey[end] == opp:
                k -= 1
                if k < 0:
                    max_len = max(max_len, end - start)
                    start += 1
                    if answerKey[start - 1] == opp:
                        k += 1
                end += 1
            else:
                end += 1

        return max_len



trial = Solution()
o = trial.maxConsecutiveAnswers(answerKey = "TFFT", k = 1)
print(o)