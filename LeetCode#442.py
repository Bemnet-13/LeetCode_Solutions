class Solution:
    def findDuplicates(self, nums):
        res = []
        sorted_nums = [-1] * len(nums)

        for i in range(len(nums)):
            if sorted_nums[nums[i] - 1] == -1:
                sorted_nums[nums[i] - 1] = nums[i]
            else:
                res.append(nums[i])
        
        return res

trial =Solution()
o = trial.findDuplicates([4,3,2,7,8,2,3,1])
print(o)