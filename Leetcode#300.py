class Solution:
    def lengthOfLIS(self, nums) -> int:
        # construct a list with enumertae(nums)
        # Sort the list with respect to the value
        # run a for loop  where we count a number as part of a subsequence if the number is is strictly greater than the previous index and the index value is greater if not continue to the next value


        indexed_nums = list(enumerate(nums))
        # indexed_nums.sort(key= lambda num:num[1])

        maximum = 0
        count = 1
        print(indexed_nums)
        for i in range(len(indexed_nums)):
            k = i
            for j in range(i + 1, len(indexed_nums)):
                if indexed_nums[k][0] < indexed_nums[j][0] and indexed_nums[k][1] < indexed_nums[j][1] and max(nums) == indexed_nums[j][1]:
                    counter = count + 1
                    maximum = max(maximum, counter)
                    continue
                if indexed_nums[k][0] < indexed_nums[j][0] and indexed_nums[k][1] < indexed_nums[j][1]:
                    count += 1
                    k = j
            maximum = max(maximum, count)
            count = 1
        
        return maximum

trial = Solution()
o = trial.lengthOfLIS([10,11,12,2])
print(o)