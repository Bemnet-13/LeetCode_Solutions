class Solution:
    def reversePairs(self, nums) -> int:
        pairs = self.mergeSort(nums)
        return pairs

    def mergeSort(self, lst):
        if len(lst) > 1:
            left = lst[:len(lst)//2]
            right = lst[len(lst)//2:]
            self.mergeSort(left)
            self.mergeSort(right)
            return self.merge(lst, left, right)

    def merge(self, arr, l, r):
        i = j = p = 0
        count = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[p] = l[i]
                p += 1
                i += 1
            else:
                if l[i] > 2* r[j]:
                    count += 1
                arr[p] = r[j]
                p += 1
                j += 1
        while i < len(l):
            arr[p] = l[i]
            p += 1
            i += 1
        while j < len(r):
            arr[p] = r[j]
            p += 1
            j += 1

        return count
    
trial = Solution()
o = trial.reversePairs(nums = [2,4,3,5,1])
print(o)