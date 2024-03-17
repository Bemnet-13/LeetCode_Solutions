class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        app = {}
        for num in nums:
            if num not in app:
                app[num] = 1
            else:
                app[num] += 1
        i = j = 0
        n = 0
        while i < len(nums):
            while n in app and j < app[n]:
                nums[i] = n
                j += 1
                i += 1
            j = 0
            n += 1