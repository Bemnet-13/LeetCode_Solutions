class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        triplets = nums[:3]
        i = 0
        while not self.valid_tri(triplets):
            i += 1
            upper = i + 3
            triplets = nums[i : upper]
            if upper == len(nums):
                break
        
        if self.valid_tri(triplets):
            return sum(triplets)
        else:
            return 0
        
        
    def valid_tri(self, triplets):
        return triplets[0] + triplets[1] > triplets[2] and triplets[1] + \
            triplets[2] > triplets[0] and triplets[2] + \
            triplets[0] > triplets[1]


trial = Solution()
o = trial.largestPerimeter([5, 2, 2])
print(o)
