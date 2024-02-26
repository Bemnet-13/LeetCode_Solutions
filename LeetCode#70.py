from itertools import combinations
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1,1,1,1,1,1,1 == 1
        # 2,2,2,1 == 4
        # 2,2,1,1,1== 10
        # 2,1,1,1,1,1 == 6 
        
        twos = n // 2
        rem = n % 2
        s = twos + rem
        count = 1
        if n == 1:
            return count 
        for i in range(s, n, 1):
            count += self.fact(i) // (self.fact(twos)* self.fact(rem))
            twos -= 1
            rem += 2

        return count
    def fact(self, num):
        mul = 1
        for i in range(1, num + 1):
            mul *= i
        return mul
trial = Solution()
o = trial.climbStairs(n = 10)
print(o)