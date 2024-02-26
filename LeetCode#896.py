class Solution:
    def isMonotonic(self, nums) -> bool:
        nums_inc = sorted(nums)
        if nums == nums_inc or nums == nums_inc[::-1]:
            return True
        return False