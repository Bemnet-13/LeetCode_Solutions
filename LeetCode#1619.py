class Solution:
    def trimMean(self, arr) -> float:
        arr.sort()
        i = int(len(arr) * 0.05)

        return sum(arr[i:len(arr)-i])/ 2*i