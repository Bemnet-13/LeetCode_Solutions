class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        # Intuition
        # Iterate through the dictionary an dstore the occurence of each element in arr
        # Sort the array by the number of occuerence
        # Iterate through the list k times
        # Split the array upto k
        # return the set of the splited array
        # [3,3,4,4,4,5,5,5]
        # [2,3,3] k = 2

        occurence = {}

        for num in arr:
            if num not in occurence:
                occurence[num] = 1
            else:
                occurence[num] += 1
        
        occ = list(occurence.values())
        occ.sort()
        print(occ)
        for i in range(len(occ)):
            k -= occ[i]
            if k < 0:
                return len(occ) - i
        return 0
            
    
trial =Solution()
o = trial.findLeastNumOfUniqueInts(arr = [1,1], k = 1)
print(o)