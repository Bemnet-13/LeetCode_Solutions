class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        t = ""
        valid_lst = []
        lst = []
        for i in s:
            t += i
            if i == "(":
                valid_lst.append(i)
            if i == ")":
                valid_lst.pop()
            if valid_lst == []:
                lst.append(t)
                t = ""
        print(lst)
        result = ""
        for i in lst:
            inner = i[1:len(i)-1]
            if inner != "":
                result += i[1:len(i)-1]
        return result
trial = Solution()
print(trial.removeOuterParentheses(s = "(()())(())"))
