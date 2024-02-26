class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        ruleKey_dict = {"type": 0, "color": 1, "name": 2}
        index = ruleKey_dict[ruleKey]
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1

        return count


trial = Solution()
output = trial.countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], [
                            "phone", "gold", "iphone"]], ruleKey="type", ruleValue="phone")
print(output)
