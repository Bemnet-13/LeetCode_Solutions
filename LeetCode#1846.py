class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr) -> int:
        # Intuition
        # Sort the array
        # Iterate through the array and check if the condition is satisfied
        # Iteate until the end of the list 
        # return the last element in the list

        arr.sort()
        if len(arr) == 1:
            return 1
        for i in range(len(arr)-1):
            if i == 0:
                arr[0] = 1
            if arr[i + 1] -arr[i] > 1:
                arr[i + 1] = arr[i] + 1
        print(arr)
        return arr[-1]
    
    
trial = Solution()
o = trial.maximumElementAfterDecrementingAndRearranging(arr = [91205])
print(o)