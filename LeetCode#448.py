class Solution:
    def findDisappearedNumbers(self, nums):
        sorted_nums = [-1] * len(nums)

        for num in nums:
            sorted_nums[num-1] = num
        
        result = []

        for i in range(len(sorted_nums)):
            if sorted_nums[i] == i + 1:
                result.append(i + 1)

        return result