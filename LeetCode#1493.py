class Solution:
    def longestSubarray(self, nums) -> int:
        # Intuition
        # Use start and end indices to locate the first and last indices that are valid 
        # in the valid string
        # use k = 1 as to store the number of elements to remove
        # if k == 1 or 0, the string is valid
        # If k == 0 and the string is not valid
        # then push start by 1 and restore k to be 1
        if len(nums) == nums.count(1):
            return len(nums) - 1
        
        start = end = max_len = 0
        k = 1

        while end < len(nums):
            if end == len(nums) - 1:
                if nums[end] == 0:
                    k -= 1
                max_len = max(max_len, end - start + k)
                break
            elif nums[end] == 0:
                k -= 1
                if k < 0:
                    max_len = max(max_len, end - start + k)
                    start += 1 
                    k = 1
                    if 0 in nums[start:end]:
                        k -= 1
                else:
                    end += 1
            else:
                end += 1
        return max_len
    

trial = Solution()
o = trial.longestSubarray(nums = [1,0,1,1,0])
print(o)