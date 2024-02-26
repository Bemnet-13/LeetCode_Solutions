import math
class Solution:
    def sequentialDigits(self, low: int, high: int):
        lower_digit = int(math.log10(low)) + 1
        upper_digit = int(math.log10(high)) + 1
        if lower_digit == upper_digit:
            return self.seqCheck(low, high, lower_digit)
        digit_lst = list(range(lower_digit, upper_digit+1))

        seq_digits = []
        for i in digit_lst:
            if i == lower_digit:
                lst = self.seqCheck(low, 9 * (10**(i-1)),i)
            elif i == upper_digit:
                lst = self.seqCheck(1 * (10**(i-1)),high,i)
            else:
                lst = self.seqCheck(1 * (10**(i-1)),9 * (10**(i-1)),i)
            
            seq_digits += lst
        return seq_digits

    def seqCheck(self, l, h, digit):
        output = []
        first_digit = l // (10**(digit-1))
        n = 0
        offset = 0
        for i in range(digit-1, -1, -1):
            n += first_digit * 10**i
            offset += 1 * 10**i
            first_digit += 1

        print((n // (10**(digit-1))) + digit)
        print(n // (10**(digit-1)))
        print(digit)
        if n >= l and n <= h and n // (10**(digit-1)) + digit > 10:
            output.append(n)
        
        if l >= h:
            return []

        last = 0

        while last <= h:
            last = n + offset
            if last // (10**(digit-1)) + digit > 10:
                break
            if last <= h:
                output.append(last)
            else:
                break
            n = output[-1]

        return output        




trial = Solution()
print(trial.sequentialDigits(low = 31365477, high = 514800930))
        