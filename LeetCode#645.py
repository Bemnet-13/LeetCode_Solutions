class Solution:
    def findErrorNums(self, nums):
        # Sort the array in cyclic sort 
        # Iterate through the array and
        # append the index in the result 
        # and the element at that index
        i = 0
        while i < len(nums):
            corr = nums[i] - 1
            if i == corr or nums[i] == nums[corr]:
                i += 1
            else:
                nums[i], nums[corr] = nums[corr], nums[i]
        res = []
        for i in range(len(nums)):
            if i != nums[i] - 1:
                res.extend([i + 1, nums[i]])
        return res


trial = Solution()
o = trial.findErrorNums([1,2,2,4])
print(o)