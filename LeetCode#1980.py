class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        # Intuition
        # Generate the integers of from the given bits
        # Generate all possible integers from by using n
        # Use set dfference
        # Return the first integer by conerting it into binary

        nums_int = set()

        for num in nums:
            nums_int.add(int(num, 2))

        print(nums_int)

        integers = set([i for i in range(len(nums[0]))])

        rem = integers - nums_int

        for i in rem:
            if i == 0:
                return len(nums[0]) * "0"
            return format(i, 'b')
        
trial = Solution()
o = trial.findDifferentBinaryString(nums = ["01","10"])
print(o)