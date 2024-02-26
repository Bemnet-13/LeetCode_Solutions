class Solution:
    def diagonalSort(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        edge_entry = [[0, i] for i in range(cols)] + [[j,0] for j in range(rows)]
        for entry in edge_entry:
            self.sortDiagonally(entry, mat)

        return mat


    def sortDiagonally(self, entry, mat):
        i, j = entry[0], entry[1]
        diagonal_arr = []
        while i < len(mat) and j < len(mat[0]):
            diagonal_arr.append(mat[i][j])
            i += 1
            j += 1
        
        diagonal_arr.sort()
        i, j = entry[0], entry[1]
        p = 0
        while i < len(mat) and j < len(mat[0]) and p < len(diagonal_arr):
            mat[i][j] = diagonal_arr[p]
            i += 1
            j += 1
            p += 1
        
        return mat
        
trial = Solution()
o = trial.diagonalSort(mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]])
print(o)