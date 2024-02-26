class Solution:
    def findFinalValue(self, nums, original):
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] == original:
                original *= 2
            i += 1
        
        return original
trial = Solution()
o = trial.findFinalValue(nums = [5,3,6,1,12], original = 3)
print