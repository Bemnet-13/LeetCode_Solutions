class Solution:
    def pivotInteger(self, n: int) -> int:
        # Intuition
        # Generate all the integers as a list and take the prefix sum of the list
        # Check if the prefix sum of the right is equal to the left with inclusive bound
        # return the integer in that index

        nums = list(range(1, n+1))
        pre_sum = [0]

        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        for i in range(1, len(pre_sum)):
            if i == 1 and pre_sum[-1] == nums[0]:
                return 1
            elif i == len(pre_sum) - 1 and nums[-1] == pre_sum[-1]:
                return i
            else:
                rsum = pre_sum[-1] - pre_sum[i-1]
                lsum = pre_sum[i]
                if lsum == rsum:
                    return i
        return -1
trial = Solution()
o = trial.pivotInteger(n = 1)
print(o)
