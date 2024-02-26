import math
class Solution:
    def countNicePairs(self, nums) -> int:
        # Intuition
        # Iterate through the nums array and for each 
        # entry the loop through the indices beyond 
        # increase count by 1 if pair satisfies property
        # Define a rev function
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + self.rev(nums[j]) == nums[j] + self.rev(nums[i]):
                    count += 1

        return count % (10**9 + 7)

    def rev(self, num):
        digit = int(math.log10(num))
        reverse = 0

        while digit >= 0:
            reverse += (num % 10) * 10** digit
            num = num // 10
            digit -= 1
        
        return reverse
        
trial = Solution()
o = trial.countNicePairs(nums = [13,10,35,24,76])
print(o)