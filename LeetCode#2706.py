class Solution:
    def buyChoco(self, prices, money) -> int:
        prices.sort()
        count = 0
        reserve = money
        for price in prices:
            count += 1
            money -= price
            if count == 2:
                break        
        if money < 0:
            return reserve
        return money
    # [1,0,1,0,1,0,1,1,0]
    # 2 + 2 = 4
    # 3 + 2 = 5
    # 1 + 4 = 5

trial = Solution()
o = trial.buyChoco(prices = [3,2,3], money = 3)
print(o)