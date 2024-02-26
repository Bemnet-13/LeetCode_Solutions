class Solution:
    def reductionOperations(self, nums) -> int:
        # Intuition
        # Sort the array 
        # Find the smallest number in the array
        # Iterate through the list
        # [1,2,2,3,3]
        # If you find an element different from the smallest number
        # Update curr and add len(nums)- i to count
        
        nums.sort()

        curr = nums[0]
        count = 0
        for i in range(len(nums)):
            if curr != nums[i]:
                curr = nums[i]
                count += (len(nums) - i)
        return count

trial = Solution()
o = trial.reductionOperations(nums = [1,1,2,2,3])
print(o)