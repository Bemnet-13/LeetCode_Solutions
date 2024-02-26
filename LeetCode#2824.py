class Solution:
    def countPairs(self, nums, target) -> int:
        right_pairs = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    pairs = tuple([i,j])
                    right_pairs.append(pairs)

        return len(right_pairs)

trial = Solution()
output = trial.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2)
print(output)