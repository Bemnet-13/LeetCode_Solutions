class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        l = 0
        r = l + 1
        min_sum = 0
        reserved = removed = None
        while r < len(colors):
            if colors[l] == colors[r]:
                if l == removed:
                    if neededTime[r] < neededTime[reserved]:
                        removed = r
                    else:
                        removed = reserved
                elif r == removed:
                    if neededTime[l] < neededTime[reserved]:
                        removed = l
                    else:
                        removed = reserved
                    
                elif neededTime[l] <= neededTime[r]:
                    removed = l
                    reserved = r
                elif neededTime[l] > neededTime[r]:
                    removed = r
                    reserved = l
                min_sum += neededTime[removed]
            l += 1
            r += 1
        return min_sum
    
trial = Solution()
o = trial.minCost(colors ="aaabbbabbbb",neededTime =[3,5,10,7,5,3,5,5,4,8,1])
print(o)