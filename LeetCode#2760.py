class Solution:
    def longestAlternatingSubarray(self, nums, threshold) -> int:
        l = 0
        m = r = l
        max_len = 0
        while r < len(nums):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                l += 1
                m = l
                r = l
            elif nums[l] % 2 == 0 and nums[l] <= threshold and l == r:
                length = r - l + 1
                max_len = max(max_len, length)
                m = l
                r = m + 1
                 
            elif nums[m] % 2 != nums[r] %2 and nums[m] <= threshold and nums[r] <= threshold:
                length = r - l + 1
                max_len = max(max_len, length)
                m = r 
                r += 1
            else:
                l += 1
                m = l
                r = m + 1
                # length = r - l + 1
                # max_len = max(max_len, length)
    
        return max_len

trial = Solution()
o = trial.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5)
print(o)