class Solution:
    def totalMoney(self, n: int) -> int:
        # Intuition
        # Find the total number of weeks for a given n
        # Find the remaining days from the week
        # Compute the result

        weeks = n // 7
        rem = n % 7

        deposit = 0
        init = 1

        while weeks > 0:
            deposit += ((2 * init + 6) * 7 )//2
            weeks -= 1
            init += 1
        
        if rem > 0:
            deposit += ((2 * init + (rem - 1)) * rem )//2
        
        return deposit

trial = Solution()
o = trial.totalMoney(4)
print(o)