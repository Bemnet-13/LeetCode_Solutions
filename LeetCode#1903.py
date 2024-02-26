class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Intutution
        # Iterate from the back of the string
        # Slice the string and check if it is odd
        # If it is return it

        for i in range(len(num),0,-1):
            number = num[:i]
            if int(number) % 2 == 1:
                return number
        return ""
    
trial = Solution()
o = trial.largestOddNumber(num = "354")
print(o)