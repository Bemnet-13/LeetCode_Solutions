class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        # Intuition
        # Generate all possible odds <= len(arr)
        # Using them as window size and window movement as 1
        # Sum up every sub array and increment it to count
        # return count

        sizes = [2*i + 1 for i in range(len(arr)) if 2*i + 1 <= len(arr)]
        count = 0

        for size in sizes:
            window_sum = sum(arr[:size])           
            for i in range(size, len(arr)):
                count += window_sum
                window_sum += arr[i]
                window_sum -= arr[i-size]
            count += window_sum
        return count
    
trial = Solution()
o = trial.sumOddLengthSubarrays(arr = [1,2])
print(o)
