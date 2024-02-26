class Solution:
    def missingNumber(self, nums) -> int:
        distincts = set(list(range(0, len(nums)+1)))
        present = set(nums)

        missing = distincts - present

        for elem in missing:
            return elem