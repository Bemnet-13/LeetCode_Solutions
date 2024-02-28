class Solution:
    def niceSubarrays(self, nums, k):
        # Intuition
        # Initalize a dictionary called counter
        # Store the number of odd in it as counter['odds']
        # Initialize a start and end index to be 0
        # Use a while loop and check if nums[end] % 2 == 1
        # If then add it to the dictionary
        # check if counter[odds] == k
        #  if it is then temp = k
        # then check the remaining indices until len(s)-1
        # if counter[odds] == k and nums[end] is odd then, increase start by one
        # and end = temp

        counter = {'odds' : 0}
        start = end = count = 0
        temp = -1

        while start < len(nums):
            if counter['odds'] == k and nums[end] % 2 == 1:
                end = temp
                temp = -1
                if nums[start] % 2 == 1:
                    counter['odds'] -= 1
                start += 1
            elif nums[end] % 2 == 1:
                counter['odds'] += 1
                end += 1        
            if counter['odds'] == k and temp == -1:
                count += 1
                temp = end - 1
                if end < len(nums) - 1:
                    end += 1
            elif counter['odds'] == k:
                count += 1
                if end == len(nums) - 1:
                    end = temp
                    if nums[start] % 2 == 1:
                        counter['odds'] -= 1                       
                    start += 1
                end += 1
            elif counter['odds'] < k and end == len(nums)-1:
                if nums[start] % 2 == 1:
                    counter['odds'] -= 1
                start += 1
            elif counter['odds'] < k and nums[end] % 2 == 0:
                end += 1
        return count
trial =Solution()
o = trial.niceSubarrays(nums = [1,1,2,1,1], k = 3)
print(o)