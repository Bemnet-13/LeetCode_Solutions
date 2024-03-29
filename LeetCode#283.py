class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = l + 1

        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            if nums[l] != 0:
                l += 1
                r += 1

        # print(nums)

trial =Solution()
trial.moveZeroes(nums = [3,0,9,6,0,7,0,0,3])


            