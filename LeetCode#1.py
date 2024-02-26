class Solution:
    def twoSum(self, nums, target: int):
        operands = [x for x in range(-1 * target,target + 1, 1)]
        
        for i in range(len(nums)):
            op = target- nums[i]
            if nums[i] in operands and op in nums:
                if nums.index(op) != i:
                    return [i, nums.index(op)]
        return []   
o = Solution()
print(o.twoSum([-3,4,3,90],0))