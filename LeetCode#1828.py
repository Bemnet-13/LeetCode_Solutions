class Solution:
    def countPoints(self, points, queries):
        count = []
        for circle in queries:
            c = 0
            for point in points:
                if (point[0] - circle[0])**2 + (point[1] - circle[1])**2 <= circle[2]**2:
                    c += 1
            count.append(c)

        return count
trial = Solution()
o = trial.countPoints( points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])
print(o)