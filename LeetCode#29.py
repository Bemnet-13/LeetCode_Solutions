import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = dividend
        d = divisor
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        if n*d < 0 and abs(d) == 1:
           return -1*2**31  if abs(n) < -1*2**31 -1 else -1 * abs(n)
        elif abs(d) == 1:
            return 2**31 - 1 if abs(n) > 2**31 -1 else abs(n)

        l = math.log10(dividend) - math.log10(divisor)
        print(l)
        quotient = 10**l
        
        if n*d < 0:
            return -1* quotient

        return quotient

trial = Solution()
o = trial.divide(8,3)
print(o)