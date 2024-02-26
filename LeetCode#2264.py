class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Intuition
        # Iterate through the list
        # Use slicing operator to slice the string and check the property
        # Append to a list if the property is satisfied 
        distinct = []
        for i in range(len(num)-3 + 1):
            sub = num[i :i + 3]
            if sub.count(sub[0]) == 3:
                distinct.append(sub)
        
        if distinct == []:
            return ""
        
        return max(distinct)

trial = Solution()
o = trial.largestGoodInteger(num = "222")
print(o)