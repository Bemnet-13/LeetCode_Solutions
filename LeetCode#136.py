class Solution:
    def singleNumber(self, nums) -> int:
        space = []

        for num in nums:
            if num in nums:
                space.remove(num)
            else:
                space.append(num)
        
        return space[0]