class Solution:
    def combinationSum(self, candidates, target: int):
        # Intuition
        # for each entry in candidiates
        # evaluate target mod candidates[i] and target // candidates[i]
        # if the results are in the candidates, then construct an array and append it to mat
        # if not run a while loop such that
        # decrease n by 1 and increase rem by candiates of i
        # check the if condition again
        # if it exists append arr to mat and break out of the while loop
        # if not run the while loop until n > 0 

        mat = []
        comb = []

        for i in range(len(candidates)):
            n = target // candidates[i]
            rem = target % candidates[i]

            if (rem in candidates):
                comb = n * [candidates[i]] + [rem]
                mat.append(comb)
                continue
            elif rem == 0:
                comb = n * [candidates[i]]
                mat.append(comb)
                continue

            while n > 0:
                rem += candidates[i]
                n -= 1
                if (rem in candidates and n != 0):
                    comb = n * [candidates[i]] + [rem]
                    mat.append(comb)
                    break
        
        comb_sum = []
        
        for arr in mat:
            arr.sort()
            if arr not in comb_sum:
                comb_sum.append(arr)

        return comb_sum
    
trial = Solution()
o = trial.combinationSum(candidates = [2,3], target = 5)
print(o)