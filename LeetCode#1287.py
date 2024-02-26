class Solution:
    def findSpecialInteger(self, arr) -> int:
        # Intutuion
        # Iterate through the list and 
        # Use count and curr variables
        # if the current element and arr[i] are the same increaase count by one
        # If not reset count to 1 and cuur to arr[i]
        # It count >= 0.25* len(nums), return curr

        curr = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == curr:
                count += 1
            if count > int(0.25*len(arr)):
                return curr

            elif arr[i] != curr:
                count = 1
                curr = arr[i]
        

trial = Solution()
o = trial.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10])
print(o)
