class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:
        # Intuition
        # Sort the ranges by its first index
        # Iterate through the sorted ranges and find the left range
        # Sum up all the elemnts to the right of and store it in the sum variable
        # Find the right in ranges and sum up all the elements upto the right
        # Use arthimetic sum to compare the computed sum to the p_sum from ranges

        ranges.sort(key = lambda range: range[0])
        summed = 0
        after = False
        for r in ranges:
            if left in range(r[0], r[1] + 1):
                if right in range(r[0], r[1] + 1):
                    return True
                else:
                    after = True
                    summed = sum(range(left,r[1] + 1))
            elif left not in range(r[0], r[1] + 1) and not after:
                continue
            elif left not in range(r[0], r[1] + 1) and after:
                if right in range(r[0], r[1] + 1):
                    summed += sum(range(r[0], right + 1))
                else:
                    summed += sum(range(r[0],r[1] + 1))
        
        if not after and summed == 0:
            return False
        
        arth_sum = (right - left + 1) * (left + right) // 2
        
        return summed == arth_sum 


trial = Solution()
o = trial.isCovered([[15,36],[15,23],[15,44],[30,49],[2,19],[27,36],[7,42],[12,41]], 19, 47)
print(o)