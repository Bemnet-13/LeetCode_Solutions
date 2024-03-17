class Solution:
    def reversePairs(self, nums) -> int:
        # Brute force approach

        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        
        return count
    
trial = Solution()
o = trial.reversePairs(nums = [2,4,3,5,1])
print(o)