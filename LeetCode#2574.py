class Solution:
    def leftRightDifference(self, nums):
        # Intuition
        # Take the prefix sum of nums
        # Use answer array to compute right and left sum

        p_sum = [nums[0]]

        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1] + nums[i])
        
        answer = []
        for i in range(len(p_sum)):
            if i == 0:
                answer.append(abs(p_sum[-1] - p_sum[i]))
            elif i == len(p_sum) - 1:
                answer.append(abs(p_sum[i - 1]))
            else:
                answer.append(abs((p_sum[-1] - p_sum[i]) - p_sum[i-1]))
        
        return answer

trial = Solution()
o = trial.leftRightDifference(nums = [1, 2, 3, 4])
print(o)

