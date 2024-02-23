class Solution:
    def returnToBoundaryCount(self, nums) -> int:
        # Intuition
        # Find the prefix sum of nums
        # COUNT THE NUMBER OF 0S IN THE PREFIX SUM ARRAY AND return it

        presum = [nums[0]]

        for i in range(1, len(nums)):
            presum.append(presum[-1] + nums[i])
        return presum.count(0)