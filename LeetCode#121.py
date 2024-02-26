class Solution:
    def maxProfit(self, prices) -> int:
        price_fut = list(enumerate(prices)).sort(key= lambda price:price[1])
        price_inc = sorted(prices)

        if prices == price_inc[::-1]:
            return 0
        
        