class Solution:
    def minStartValue(self, nums) -> int:
        # Intuition
        # Find the prefix sum of nums
        # Find the minimum value of the prefix sum
        # If the number is negative or zero, return  abs(min) + 1
        # If the number is positive, return 1

        accumulator = 0
        p_sum = [0] * len(nums)
        for i in range(len(nums)):
            accumulator += nums[i]
            p_sum[i] = accumulator
        
        minimum = min(p_sum)

        if minimum <= 0:
            return abs(minimum) + 1
        else:
            return 1