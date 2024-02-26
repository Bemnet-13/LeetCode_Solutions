import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if abs(x) != x:
            return False
        digit = int(math.log10(x))
        num = x
        palindrome = 0
        while digit >= 0:
            rem = num % 10
            num = num // 10
            palindrome += rem * 10**digit
            digit -= 1
        return palindrome == x
        

trial = Solution()
print(trial.isPalindrome(-2222))