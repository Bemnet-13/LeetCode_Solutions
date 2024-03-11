class Solution:
    def findDisappearedNumbers(self, nums): 
        result = []
        i = 0

        while i < len(nums):
            idx = nums[i] - 1
            if i == nums[i] + 1:
                i += 1
            else:
                nums[i], nums[idx] = nums[idx], nums[i]
        
        for i in range(len(nums)):
            if i != nums[i] - 1:
                result.append(i + 1)
        return result
    
trial = Solution()
o = trial.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(o)