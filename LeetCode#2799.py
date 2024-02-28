class Solution:
    def countCompleteSubarrays(self, nums) -> int:
        # Intuition
        # Store the number of the set of nums in a variable distinct
        # Define an empty dictionary
        # Use start and end indices intialized to 0
        # Slide end until the len(dictionary) == distinct 
        # If it does, add len(nums) - end to count
        # Shift start by 1 and decrease its appearance
        distinct= len(set(nums))
        appear = {}
        start = end = count = 0

        while start < len(nums):
            if nums[end] not in appear:
                appear[nums[end]] = 1
            else:
                appear[nums[end]] += 1
            if end < len(nums):
                end += 1
            if len(appear) == distinct:
                end -= 1
                count += len(nums) - end
                appear[nums[end]] -= 1
                if appear[nums[start]] > 0:
                    appear[nums[start]] -= 1
                if appear[nums[end]] == 0:
                    del appear[nums[end]]
                
                if len(appear) == 0:
                    pass
                elif appear[nums[start]] == 0:
                    del appear[nums[start]]
                start += 1
                if start > end:
                    end = start
                
            elif end == len(nums):
                end -= 1
                appear[nums[end]] -= 1
                if appear[nums[start]] > 0:
                    appear[nums[start]] -= 1
                if appear[nums[end]] == 0:
                    del appear[nums[end]]
                if len(appear) == 0 or nums[start] not in appear:
                    pass
                elif appear[nums[start]] == 0:
                    del appear[nums[start]]
                start += 1

        return count


trial =Solution()
o = trial.countCompleteSubarrays([1917,1917,608,608,1313,751,558,1561,608])
print(o)