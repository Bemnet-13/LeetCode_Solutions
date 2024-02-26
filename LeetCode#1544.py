class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if len(stack) == 0:
                stack.append(s[i])
                i += 1
            elif stack[-1] != s[i] and (stack[-1].lower() == s[i] or stack[-1].upper() == s[i]):
                stack.pop()
                i += 1
                continue
            else:
                stack.append(s[i]) 
                i += 1
        
        return "".join(stack)

trial = Solution()
print(trial.makeGood(s = "s"))