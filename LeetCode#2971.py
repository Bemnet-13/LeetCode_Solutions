class Solution:
    def largestPerimeter(self, nums) -> int:
        # Intutition
        # Sort the array nums
        # Store the prefix sum of the nums array on a separate array
        # Check if nums[i] > prefix_sum[i]
        # It is break the loop ans check if the prefic_sum[i] is above size 3
        # If it is return the perimeter value
        # Else return -1

        nums.sort()
        perimeter = [""] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                perimeter[i] = nums[i]
            else:
                perimeter[i] = perimeter[i-1] + nums[i]
        
        print(perimeter)
        print(nums)

        poly_perimeter = -1

        for i in range(len(nums) - 1 , 1, -1):
            if nums[i] < perimeter[i-1]:
                poly_perimeter = perimeter[i]
                break
        
        return poly_perimeter

trial = Solution()
o = trial.largestPerimeter(nums = [1,12,1,2,5,50,3])
print(o)

