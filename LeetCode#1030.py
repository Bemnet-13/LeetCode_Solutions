class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int):
        matrix = [[i, j] for i in range(rows) for j in range(cols)]

        matrix.sort(key = lambda item: abs(item[0] - rCenter) + abs(item[1] - cCenter))
        return matrix

trial = Solution()
o = trial.allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2)
print(o)