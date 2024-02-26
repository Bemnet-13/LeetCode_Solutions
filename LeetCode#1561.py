class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort(reverse=True)
        max_sum = 0
        i, k = 0, len(piles) - 1
        j = i + 1
        while k - j >= 1:
            max_sum += piles[j]
            i += 2
            j += 2
            k -= 1
        return max_sum


trial = Solution()
o = trial.maxCoins(piles = [9,8,7,6,5,1,2,3,4])
print(o)
