class Solution:
    def firstMissingPositive(self, nums) -> int:
        # FInd the least non-negative -number in the array and store it in k
        # Use cyclic Sort to sort the array
        # Iterate through the sorted array to return the least number with element-index mismatch

        k = max(nums)
        p = k
        for num in nums:
            if num > 0:
                k = min(k, num)     
        i = 0
        while i < len(nums):
            corr = nums[i] - k
            if i == corr or nums[i] <= 0 or corr > len(nums) -1 or nums[i] == nums[corr]:
                i += 1
            else:
                nums[i], nums[corr] = nums[corr], nums[i]
        print(nums)
        if nums[0] != 1:
            return 1
        for i in range(len(nums)):
            if i + k != nums[i]:
                return i + k
        return p + 1
trial =Solution()
o = trial.firstMissingPositive([2,1])
print(o)