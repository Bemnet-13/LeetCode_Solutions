class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        # Intuition
        # iterate through the points
        # Find the vector difference between the towo vectors
        # Find the minimum of the two and increment it 
        # Find the maximum of the two and increment the difference between the maximum and the minimum
        # increment to the answer

        min_time = 0

        for i in range(len(points)-1):
            x_diff = abs(points[i+1][0] - points[i][0])
            y_diff = abs(points[i+1][1] - points[i][1])

            min_time += min(x_diff,y_diff) + (max(x_diff,y_diff)-min(x_diff,y_diff))

        return min_time

trial = Solution()
o = trial.minTimeToVisitAllPoints(points = [[3,2],[-2,2]])
print(o)
