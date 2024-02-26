import math
class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        if x == 0:
            return 0

        print(2**31)
        if x > 2**31 -1 and x < -1*2**31 :
            return 0
        
        digit = int(math.log(y, 10))

        reverse = 0

        while digit >= 0:
            rem = y % 10
            y = y // 10
            reverse += rem * 10**digit
            digit -= 1
        
        return -1 * reverse if x < 0 else reverse

trial = Solution()
o = trial.reverse(1534236469)
print(o)