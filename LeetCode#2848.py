class Solution:
    def numberOfPoints(self, nums) -> int:
        # Intuition
        # Initialize a set called covered to be empty
        # Iterate through nums and update covered to be union of the range of the set 
        # return the length of the set

        covered = set()

        for num in nums:
            covered = covered | set(range(num[0], num[1] + 1))
        return len(covered)
    