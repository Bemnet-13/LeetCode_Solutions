import math
class Solution:
    def numSquares(self, n: int) -> int:
        # Intuition
        # Generate a list of valid perfect squares
        # Define squareSum(list, n) function that computes the least amount of perfect squares that sum up to a perfect square
        # Call the function by slicing the list one at a time
        # return the minimum
        m = int(math.sqrt(n))
        valid_srs = [i**2 for i in range(1,m+1)]

        minimum = n

        for i in range(m):
            output = self.squareSum(valid_srs[:m-i], n)
            minimum = min(minimum, output)
        return minimum
    
    def squareSum(self, lst, target):
        count = 0
        i = len(lst) -1
        while i >= 0:
            count += target // lst[i]
            if target >= lst[i]:
                target = target % lst[i]
            i -= 1
        
        return count

trial = Solution()
o = trial.numSquares(43)
print(o)

# 