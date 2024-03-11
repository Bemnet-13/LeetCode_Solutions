class Solution:
    def findDisappearedNumbers(self, nums): 
        i = 0
        while i < len(nums):
            corr = nums[i] - 1
            if i == corr or nums[corr] == nums[i]:
                i += 1
            else:
                nums[corr], nums[i] = nums[i], nums[corr]

        res = []
        for i in range(len(nums)):
           if i != nums[i] - 1:
               res.append(i + 1)
        return res
    
trial = Solution()
o = trial.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(o)