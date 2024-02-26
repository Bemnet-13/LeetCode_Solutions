class Solution:
    # def sortArrayByParity(self, nums):
    #     nums.sort()
    #     new_nums = []
    #     for num in nums:
    #         if num % 2 == 0:
    #             new_nums.append(num)
    #     for num in nums:
    #         if num % 2 != 0:
    #             new_nums.append(num)

    #     return new_nums
    

    def sortArrayByParity(self, nums):
        i = 0
        j = len(nums) -1 
        while i < j:
            if nums[i] % 2 != 0 and nums[j] % 2 ==0:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 != 0:
                j += 1

        return nums
    
    
