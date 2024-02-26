class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()

        i = 0
        j = i + 1
        max_sum = 0
        for i in range(0, len(nums), 2):
            if nums[i] < nums[j]:
                max_sum += nums[i]
                j += 2
            else:
                max_sum += nums[j]
                j += 2
        return max_sum
