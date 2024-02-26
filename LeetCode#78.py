from itertools import combinations
class Solution:
    def subsets(self, nums):
        # Intuition
        # Append an empty list and the list itself to the list
        subset = []
        subset.append([])
        subset.append(nums)

        for i in range(1,len(nums)):
            comb = combinations(nums, i)
            for c in list(comb):
                subset.append(list(c))
        return subset

trial = Solution()
o = trial.subsets(nums = [0])            
print(o)