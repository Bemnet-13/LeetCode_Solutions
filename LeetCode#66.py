class Solution:
    def plusOne(self, digits):
        # Intuition
        # Iterate through each digit and construct the integer from the array
        # by digits[i] * 10 **len(digits)-i
        # increment 1 to num
        # use a for loop and modulo to pop each digit out ofnum
        # append it ot a list
        # return the list
        num = 0
        for i in range(len(digits)):
            num += int(digits[i]) * 10**(len(digits)-i-1)
        num += 1

        arr = []
        while num != 0:
            rem = num % 10
            num = num // 10
            arr.append(rem)
        return arr[::-1]

trial = Solution()
o = trial.plusOne(digits = [9,9])
print(o)
