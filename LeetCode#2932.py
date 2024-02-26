class Solution:
    def maximumStrongPairXor(self, nums) -> int:
        l = 0
        max_xor = 0
        while l < len(nums):
            r = l
            for idx in range(r,len(nums)):
                if abs(nums[l]-nums[r]) <= min(nums[l], nums[idx]):
                    max_xor = max(max_xor, nums[l]^nums[idx])
            l += 1
        
        return max_xor
    
trial = Solution()
o = trial.maximumStrongPairXor()
print(o)