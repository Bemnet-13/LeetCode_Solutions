class Solution:
    def findMatrix(self, nums):
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        print(dict)
        mat = []
        arr = []
        print(sum(dict.values()))

        while sum(dict.values()) > 0:
            for item in dict:
                if dict[item] >= 1:
                    arr.append(item)
                    dict[item] -= 1
            mat.append(arr)
            arr = []
        return mat
        
        
       

trial = Solution()
o = trial.findMatrix([1,3,4,1,2,3,1])
print(o)