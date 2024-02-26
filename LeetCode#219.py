class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        nums_idx = list(enumerate(nums))
        nums_idx.sort(key = lambda item:item[1])
        l = 0
        r = l + 1
        while r < len(nums_idx):
            if nums_idx[l][1] == nums_idx[r][1] and abs(nums_idx[l][0] - nums_idx[r][0]) <= k:
                return True
            l += 1
            r += 1
        return False

trial = Solution()
o = trial.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
print(o)