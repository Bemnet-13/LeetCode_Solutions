class Solution:
    def rob(self, nums) -> int:
        money = list(enumerate(nums))
        money.sort(key = lambda mon:mon[1], reverse = True)

        maximum = 0
        for i in range(len(money)):
            count = 0
            for j in range(i, len(money)):
                if j == i:
                    count += money[j][1]
                    ind = j
                else:
                    if abs(money[j][0] - money[ind][0]) != 1:
                        count += money[j][1]
                        ind = j

            maximum = max(count, maximum)
        
        return maximum
    

trial = Solution()
o = trial.rob(nums = [2,7,9,3,1])
print(o)
