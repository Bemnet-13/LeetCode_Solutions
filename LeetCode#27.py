class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        j = 1
        while j < len(nums):            
            if nums[j] != val and nums[i] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

