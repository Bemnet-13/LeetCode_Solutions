class Solution:
    def removeDuplicates(self, nums) -> int:
        last = nums[-1]
        
        i = 0
        j = 1
        while i < len(nums):
            if nums[i] == last:
                i += 1
                for k in range(i + 1,len(nums)):
                    nums[k] = "_"
                return i
            elif nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
o = Solution()
print(o.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))