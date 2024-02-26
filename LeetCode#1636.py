class Solution:
    def frequencySort(self, nums):
        nums.sort(reverse = True)
        frequency = []
        for num in nums:
            frequency.append(nums.count(num))
        
        freq_distribution = list(zip(nums, frequency))
        freq_distribution.sort(key = lambda item: item[1])
        
        for i in range(len(freq_distribution)):
            nums[i] = freq_distribution[i][0]
        
        return nums


trial = Solution()
print(trial.frequencySort(nums=[-1,1,-6,4,5,-6,1,4,1]))
