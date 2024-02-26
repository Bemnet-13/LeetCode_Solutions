class Solution:
    def removeStars(self, s: str) -> str:
        # define a list called stack
        # for each element that is not a star , push it to stack
        # if elem == '*' , then pop an item from the stack

        stack = []
        if len(s) == 1 and s[0] == '*':
            return ""
        for chr in s:
            if chr != '*':
                stack.append(chr)
            else:
                stack.pop()
        return "".join(stack) 
trial = Solution()
o = trial.removeStars(s = "erase*****")
print(o)