class Solution:
    def kWeakestRows(self, mat, k):
        soldier_count = []
        for row in mat:
            soldier_count.append(row.count(1))
        rows = [*range(len(mat))]

        rows.sort(key=lambda i: soldier_count[i])

        return rows[:k]


trial = Solution()
o = trial.kWeakestRows(mat=[[1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 0],
                            [1, 0, 0, 0, 0],
                            [1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 1]],
                       k=3)
print(o)
