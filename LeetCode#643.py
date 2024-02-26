class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            max_avg = max(max_avg,(window_sum/k))

        return max_avg
trial = Solution()
o = trial.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
print(o)