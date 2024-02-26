class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Intuition 
        # make the length of the string s equal by adding leding zeros to the shorter string
        # Use a while loop to iterate backwards
        # Use binary addition principles
        # store the immediate result and concatenate it to sum
        # add a carry variable in case there is carry = 1
        # return sum
        # 101   
        # 110
        if len(a) > len(b):
            b = (len(a)-len(b)) * "0" + b
        elif len(a) < len(b):
            a = (len(b)-len(a)) * "0" + a

        sum = ""
        i = len(a) -1
        carry = "0"
        while i >= 0:
            if a[i] == "1" and b[i] == "1" and carry == "1":
                sum ="1" + sum
                carry = "1"
            elif a[i] == "1" and b[i] == "1":
                sum = "0" + sum
                carry = "1"
            elif a[i] == "0" and b[i] == "0" and carry == "1":
                sum = "1" + sum
                carry = "0"
            elif a[i] == "0" and b[i] == "0":
                sum = "0" + sum
                carry = "0"
            elif (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0") and carry == "1":
                sum = "0" + sum
                carry = "1"
            elif (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0"):
                sum ="1" + sum
                carry = "0"
            i -= 1
        
        if carry == "1":
            return carry + sum
        return sum   

trial = Solution()     
o = trial.addBinary(a = "1", b = "0")
print(o)