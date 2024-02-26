class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        x = sorted([point[0] for point in points])
        l = 0
        r = l + 1
        area = 0
        while r < len(x):
            if x[l] != x[r] and abs(x[l] - x[r]) > area:
                area = abs(x[l] - x[r])
            l += 1
            r += 1

        return area


trial = Solution()
o = trial.maxWidthOfVerticalArea(
    points=[[8,7],[9,9],[7,4],[9,7]])
print(o)
