class Solution:
    def largestAltitude(self, gain) -> int:
        # Intuition
        # Find the prefix sum of the gain
        # return the maximum value from heights

        heights = [0] * (len(gain) + 1)

        for i in range(len(gain)):
            heights[i + 1] = heights[i] + gain[i]
        return max(heights)