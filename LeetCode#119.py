class Solution:
    def getRow(self, rowIndex: int):
        # Intuition
        # Initialize a matrix with [[1],[1,1]]
        # Iterate through the matrix and add additional row at the end
        # If the length is equal to rowIndex return mat[-1]

        triangle = [[1],[1,1]]

        if rowIndex == 0 or rowIndex == 1:
            return triangle[rowIndex]

        at_bottom = False
        while not at_bottom:
            curr_row = triangle[-1]
            new_row = [""] * (len(curr_row) + 1)
            new_row[0] = 1
            new_row[-1] = 1 
            for i in range(1,len(curr_row)):
                new_row[i] = curr_row[i-1] + curr_row[i]
            triangle.append(new_row)
            if len(triangle) + 1 == rowIndex:
                return triangle[-1]
            
trial = Solution()
o = trial.getRow(2)
print(o)