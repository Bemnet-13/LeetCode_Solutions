class Solution:
    def findDuplicate(self, nums) -> int:
        sorted_nums = [-1] * len(nums)

        for i in range(len(nums)):
            if sorted_nums[nums[i] - 1] == -1:
                sorted_nums[nums[i] - 1] = nums[i]
            else:
                return nums[i]


trial = Solution()
o = trial.findDuplicate (nums = [3,3,3,3,3])
print(o)