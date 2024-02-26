class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        bools = []
        i = 0
        while i < len(l):
            sub_nums = nums[l[i]: r[i] + 1]
            result = self.isArthimetic(sub_nums)
            bools.append(result)
            i += 1
        return bools
    
    def isArthimetic(self, seq):
        seq.sort()
        d = seq[1] - seq[0]
        for i in range(2, len(seq)):
            if seq[i] - seq[i-1] != d:
                return False
        return True
        
trial = Solution()
o = trial.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
print(o)     

        