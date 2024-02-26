class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        r = k
        sub_aum = sum(arr[:k])
        count = 0
        while r < len(arr):
            avg = sub_aum /k 
            if avg >= threshold:
                count += 1
            sub_aum += arr[r]
            sub_aum -= arr[r -k]
            r += 1
        avg = sub_aum / k
        if avg >= threshold:
            count +=1
        return count

trial = Solution()
o = trial.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)
print(o)