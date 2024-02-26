class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        maximum = 0
        while l < r:
            sum = nums[l] + nums[r]
            maximum = max(maximum, sum)
            l += 1
            r -= 1
        return maximum