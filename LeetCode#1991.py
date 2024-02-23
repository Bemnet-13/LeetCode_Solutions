class Solution:
    def findMiddleIndex(self, nums) -> int:
        # Intuition
        # Find the prefix sum of the array
        # Iterate through the prefix sum of the arra and find the middle index

        p_sum = [nums[0]]

        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1] + nums[i])
        
        for i in range(len(p_sum)):
            if i == 0 and p_sum[-1] - p_sum[i] == 0:
                return i
            elif i == len(p_sum) - 1 and p_sum[i-1] == 0:
                return i
            else:
                rsum = p_sum[-1] - p_sum[i]
                lsum = p_sum[i-1]
                if rsum == lsum:
                    return i
        return -1