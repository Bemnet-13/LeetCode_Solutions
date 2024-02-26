class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.multiply(1, x, n, n)
    
    def multiply(self, product, x, n, k):
        if abs(n) == 0 and k > 0:
            return product
        elif abs(n) == 0 and k < 0:
            return 1/product
        return self.multiply(product * x,  x, abs(n) - 1, k)
    
trial = Solution()
print(trial.myPow(2, -4))


def myPow(self, x: float, n: int) -> float:
    product = 1
    values = (x for _ in range(abs(n)))
    for x in values:
        product *= x
    if n < 0:
        return 1 / product
    return product


