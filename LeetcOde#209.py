class Solution:
    def minSubArrayLen(self, target, nums):
        l = r = sub_sum = 0
        nums.append(0)
        min_size = len(nums)

        while r < len(nums):
            if sub_sum < target:
                sub_sum += nums[r]
                r += 1
            else:
                min_size = min(min_size, r-l)
                sub_sum -= nums[l]
                l += 1
        
        if sub_sum < target and min_size == len(nums):
            min_size = 0
        return min_size

trial = Solution()
o = trial.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
print(o)