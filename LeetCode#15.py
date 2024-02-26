import itertools
class Solution:
    def threeSum(self, nums):
        nums.sort()
        idx = -1
        negative = []
        positive = []
        if 0 in nums:
            idx = nums.index(0)
            negative = nums[:idx]
            positive = nums[idx + 1:]
        else:
            for i in range(len(nums)):
                if nums[i] < 0 and nums[i+1] >0:
                    idx = i
                    negative = nums[:idx + 1]
                    positive = nums[idx + 1:]
                    break
    
        neg_combination = list(itertools.combinations(negative, 2))
        pos_combination = list(itertools.combinations(positive, 2))
        print("positive", positive)
        print("pos_combination", pos_combination)
        print("negative", negative)
        print("neg_combination", neg_combination)
        if 0 in nums:
            return (self.withZero(idx, nums)) + self.withNoZero(neg_combination, positive, -1) + self.withNoZero(pos_combination, negative, 1)
        else:
            return self.withNoZero(neg_combination, positive, -1) + self.withNoZero(pos_combination, negative, 1)
       
       
        # print(idx)
        # print(nums)
        # # print(self.withZero(idx, nums))

        # print(self.withNoZero(neg_combination, positive, -1))
        # print(self.withNoZero(pos_combination, negative, 1))



    def withZero(self, idx, nums):
        triplets = []
        arr = []
        l = idx - 1
        r = idx + 1
        while l > 0 or r < len(nums):
            if abs(nums[l]) == nums[r] and nums[l] != nums[r]:
                arr.append(nums[l])
                arr.append( 0)
                arr.append(nums[r])

                triplets.append(arr)
                l -= 1
                r += 1
            elif abs(nums[l]) > nums[r]:
                r += 1
            elif abs(nums[l]) < nums[r]:
                l -= 1
        return triplets
        
    def withNoZero(self, comb, arr, sign):
        triplets = []
        arr_duo = []
        for duo in comb:
            if sign * sum(duo) in arr:
                ind = arr.index(sign*sum(duo))
                arr_duo.append(arr[ind])
                arr_duo.extend(list(duo))
                triplets.append(arr_duo)
        return triplets




trial = Solution()
o = trial.threeSum(nums = [0,1,1])
print(o)
        