class Solution:
    def missingNumber(self, nums) -> int:
        i = 0
        while i < len(nums):
            corr = nums[i]

            if i == corr or corr > len(nums) - 1:
                i += 1
            else:
                nums[corr], nums[i] = nums[i], nums[corr]
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

 