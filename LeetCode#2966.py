class Solution:
    def divideArray(self, nums, k: int):
        nums.sort()
        mat = []
        for i in range(0,len(nums) + 1,3):
                if i != len(nums):
                    splited = nums[i:i+3]
                    mat.append(splited)
        
        for arr in mat:
            if not (arr[1] - arr[0] <= k and  arr[2] - arr[1] <= k and arr[2] - arr[0] <= k):
                 return []
        return mat
    
trial = Solution()
o = trial.divideArray(nums = [1,3,3,2,7,3], k = 3)
print(o)
