class Solution:
    def simplifyPath(self, path: str) -> str:
        # define an empty set
        # iterate through the lis by each character
        # if character is ., continue
        # if not push it to the stack
        # peek at the stack each time and if the current chr is '/', continue
        # return the joined string
                
        stack = []
        for i in range(len(path)):
            chr = path[i]
            if len(stack) == 0:
                stack.append(chr)
            elif chr == '.':
                continue
            elif stack[-1] == "/" and chr == '/' and i != len(path) -1:
                continue
            elif stack[-1] == "/" and chr == '/' and i == len(path) -1:
                stack.pop()
            elif i == len(path)-1 and chr == '/':
                continue
            else:
                stack.append(chr)
        
        return "".join(stack)

trial = Solution()
print(trial.simplifyPath(path = "/../..."))