# Method
# Reverse sort the array
# Use two pointers l and r
# Initialize sum_left and sum_right to 0
# Using while loop iterate through the elements from left and right
# If sum left > sum right then stop looping and return sum_left


class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        print(nums)

        sum_left = sum_right = l = 0
        r = len(nums) - 1

        valid_subsequence = False

        while not valid_subsequence:
            sum_left += nums[l]
            sum_right = sum(nums) - sum_left
            l += 1
            r -= 1
            print(sum_left, sum_right)
            if sum_left > sum_right:
                valid_subsequence = True

        if l < len(nums):
            return nums[:l]
        else:
            return nums


trial = Solution()
print(trial.minSubsequence(nums=[4, 4, 7, 6, 7]))
