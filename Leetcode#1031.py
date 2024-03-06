class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        # Intuition
        # Use two sliding windows with windowSize of firstLen and secondLen
        # Use nested loop to slide the latter window
        # then with each iteration slide the first window by 1
        # then