class Solution:
    def findLHS(self, nums) -> int:
        # Intuition
        # Sort the array
        # Use sliding window
        # Is nums[end] - nums[start] <= 1 then increase end
        # else increase start by 1 until nums[end] - nums[start] <= 1
        # then increase end by 1 ...

        nums.sort()

        start = 0
        end = 0
        max_len = 0

        while end < len(nums):
            if end == len(nums) - 1 and nums[end] - nums[start] == 1:
                max_len = max(max_len, end - start + 1)
                break
            if nums[end] - nums[start] <= 1:
                end += 1
            else:
                if end - start == 1:
                    max_len = max(max_len, 0)
                elif nums[end - 1] - nums[start] == 1:
                    max_len = max(max_len, end - start)
                start += 1
        return max_len
    
trial = Solution()
o = trial.findLHS([1,4,1,3,1,-14,1,-13])
print(o)