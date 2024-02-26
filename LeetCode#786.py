class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        mat = []        
        for i in range(len(arr)):
            for j in range(len(arr)-1, i,-1):
                lst = arr[i], arr[j]
                mat.append(lst)
            if len(mat) >= k+1:
                break

        mat.sort(key= lambda item: item[0]/item[1])
        return list(mat[k-1])

trial = Solution()
o = trial.kthSmallestPrimeFraction([1,3,5,7,19,23],3)
print(o)