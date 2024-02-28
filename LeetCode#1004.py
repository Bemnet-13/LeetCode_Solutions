class Solution:
    def longestOnes(self, nums, k: int) -> int:
        start = end = count = 0
        max_len = 0
        while end < len(nums):
            # If k >= 0 then slide end by one record the max length 
            # each time k < 0 then increase start by one and if nums[start] == 0 the k += 1
            if k >= 0:
                if nums[end] == 0:
                    k -= 1
                end += 1
            else:
                if nums[start] == 0:
                    k += 1
                start += 1
            
            if k < 0:
                max_len = max(max_len, end - start + k)
            else:
                max_len = max(max_len, end - start)

        return max_len

trial = Solution()
o = trial.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
print(o)