class Solution:
    def mySqrt(self, x: int) -> int:
        # Intuition
        # Pass a high and low to a function and a target
        # If the difference between high and low is 1, return the low
        if x == 0:
            return 0
        if x == 1:
            return 1
        nearestRoot = self.nearestSquare(1, x, x)
        return nearestRoot

    def nearestSquare(self, low, high, x):
        mid = (low + high) // 2

        if mid ** 2 == x:
            return mid
        elif high - low == 1:
            return low
        elif mid ** 2 > x:
            return self.nearestSquare(low, mid, x)
        else:
            return self.nearestSquare(mid, high, x)
        
trial = Solution()
o = trial.mySqrt(36)
print(o)