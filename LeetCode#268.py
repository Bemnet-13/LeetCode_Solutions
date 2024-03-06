class Solution:
    def missingNumber(self, nums) -> int:
        i = 0
        new = [-1] * (len(nums) + 1) 
        for num in nums:
            new[num] = num
        for i in range(len(new)):
            if new[i] == -1:
                return i

 