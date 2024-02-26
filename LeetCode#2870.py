class Solution:
    def minOperations(self, nums) -> int:
        # Count the appearance of each int
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        print(dict)
        if 1 in dict.values():
            return -1
               
        count = 0
        for item in dict:
            freq = dict[item]
            maximum = 0 
            rng = freq // 3
            pas = False
            if freq % 3 == 0:
                count += freq // 3
                continue
            if freq % 2 == 0 and freq % 3 != 0:
                for i in range(1, rng+1):
                    a1 = 3 * i
                    if (freq - a1) % 2 == 0:
                        pas = True
                        maximum = max(i, maximum)

                if maximum != 0 or pas:
                    count += maximum + (freq - 3*maximum)//2       
                        
                
            if freq % 2 == 0 and not pas:
                count += freq // 2
            if freq % 2 != 0 and freq %3 != 0:
                count += freq // 3 + 1
        
        return count

trial = Solution()
o = trial.minOperations([11,11,11,11,19,11,11,11,11,11,19,11,11,11,11,11,19])
print(o)

# 14 = 3 * 4 + 2*1
# 10 = 3*2+2*2
#  20 = 3*6 + 2