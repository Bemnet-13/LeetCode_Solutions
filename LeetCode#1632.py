class Solution:
    def decrypt(self, code, k: int):
        # Intuition
        # Concatenate code into code
        # Using sliding window and k as window size itearte through the concatenated code
        # And append it to the list
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            return self.posDecrypt(k, code)
        else:
            return self.negDecrypt(abs(k), code)
        
    def posDecrypt(self, k, code):
        circled = 2* code
        window_sum = sum(circled[1:k + 1])
        decrypted = [window_sum]

        for i in range(1, len(code)):
            
            window_sum += circled[k + i]
            window_sum -= circled[i]
            decrypted.append(window_sum)
        return decrypted
    def negDecrypt(self, k, code):
        circled = 2* code
        window_sum = sum(circled[len(code)- k:len(code)])
        decrypted = [window_sum]

        for i in range(len(code), len(circled) - 1):
            window_sum += circled[i]
            window_sum -= circled[i - k]
            decrypted.append(window_sum)
        return decrypted
    
trial = Solution()
o = trial.decrypt(code = [2,4,9,3], k = -2)
print(o)