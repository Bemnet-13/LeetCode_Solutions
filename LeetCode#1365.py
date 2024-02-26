class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        list_less = []
        for num in nums:
            count = 0
            i = 0
            found = True
            while found:
                if sorted_nums[i] < num:
                    i += 1
                    count += 1
                else:
                    list_less.append(count)
                    break
        return list_less
