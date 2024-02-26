class Solution:
    def answerQueries(self, nums, queries):
        # Intuition
        # Sort the array nums
        # Find the prefix sum of nums and store it in p_sum
        # Iterate through p_sum using a while loop and use pointers
        # i and j
        # If p_sum[i] <= queries[j] and p_sum[i + 1] > queries[j]
        # then append i + 1 to the answer and increment j by 1
        # else increment i by 1

        nums.sort()
        # queries.sort()
        p_sum = [nums[0]]

        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1] + nums[i])
        
        i = 0
        r = 0
        ans = []

        while i < len(p_sum) and r < len(queries):
            # print(p_sum[i + 1])
            if p_sum[i] <= queries[r] and (i + 1 >= len(nums) or p_sum[i + 1] > queries[r]):
                r += 1
                ans.append(i + 1)
            elif p_sum[i] <= queries[r]:
                i += 1
            else:
                if i - 1 < 0:
                    ans.append(0)
                    r += 1
                else:
                    ans.append(i)
                    r += 1
        
        return ans 







trial = Solution()
o = trial.answerQueries(nums = [736411,184882,914641,37925,214915], queries = [331244,273144,118983,118252,305688,718089,665450])
print(o)







        # nums.sort()
        # queries.sort()
        # i = 0
        # r = 0
        # answer = []

        # while i < len(queries):
        #     if nums[r] > queries[i] and i == 0:
        #         answer.append(r)
        #         i += 1
        #     # elif nums[r] <= nums[i] and r == 0:
        #     #     r += 1
        #     elif sum(nums[:r]) < queries[i]:
        #         r += 1
        #     else:
        #         answer.append(r)
        #         i += 1
        #         r = 0

        # return answer

