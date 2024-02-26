class Solution:
    def maxIceCream(self, costs, coins) -> int:
        max_cost = int(max(costs))
        min_cost = int(min(costs))
        arr = ['']* int(max_cost - min_cost + 1)
        for i in range(min_cost, max_cost + 1):
            arr[i-min_cost] = costs.count(i)

        max_no = 0
        k = 0
        while k < len(arr):
            max_no += (k+min_cost) * arr[k]
            if max_no <= coins:
                k += 1
            elif k == 0:
                return k   
            else:
                return k + 1     
        return k

trial = Solution()
o = trial.maxIceCream(costs = [1,3,2,4,1], coins = 7)
print(o)
