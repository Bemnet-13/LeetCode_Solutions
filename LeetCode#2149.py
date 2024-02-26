class Solution:
    def rearrangeArray(self, nums):
        # Intuition
        # Append each positive number to a positive list and negtaive too
        # Prpare a new list and append each of the list respectively


        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        for i in range(len(nums)//2):
            j = 2* i

            nums[j] = positive[i]
            nums[j+1] = negative[i]
        
        return nums
    
trial = Solution()
o = trial.rearrangeArray(nums = [1,-1])
print(o)