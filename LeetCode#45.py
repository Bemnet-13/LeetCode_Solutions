class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # [1,2,3,4,6]
        # Use binary search to use log n algorithm
        # After dividing the array, return the index m if nums[m] == target
        # If not compare the indices and place the target on the index
        result = self.binarySearch(nums, 0, len(nums) -1, target)
        return result
    def binarySearch(self,arr, low, high, target):
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif low == mid and mid == high:
            return mid
        elif arr[mid] < target:
            return self.binarySearch(arr, mid + 1, high, target)
        else:
            return self.binarySearch(arr, low, mid, target)

trial = Solution()
o = trial.searchInsert(nums = [1,2,3,4,6], target = 5)
print(o)