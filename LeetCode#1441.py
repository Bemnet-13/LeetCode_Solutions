class Solution:
    def buildArray(self, target, n: int):
        stack = []
        comp = []
        for num in range(1, n+1):
            stack.append("push")
            comp.append(num)
            if comp == target:
                break
            if num not in target:
                stack.append("pop")
                comp.pop()   
        return stack

trial = Solution()
o = trial.buildArray(target = [1,3], n = 3)
print(o)