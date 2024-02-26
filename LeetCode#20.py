class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'(':')', '{':'}', '[' : ']'}
        stack = []
        for chr in s:
            if len(stack) == 0:
                stack.append(chr)
            else:
                if dictionary[stack[-1]] == chr:
                    stack.pop()
        
        return len(stack) == 0
    
    