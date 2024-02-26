class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        min_score = nums[len(nums)-1] - nums[0]
        l = 0
        r = k
        while r < len(nums):
            score = nums[r] - nums[l]
            min_score = min(min_score, score)
            l += 1
            r += 1
        return min_score