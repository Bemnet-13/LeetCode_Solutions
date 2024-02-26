class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Intuition
        # Iterate through the matrix with for loop
        # Iterate through each array and store the matrix
        # Return it
        # matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # Output: [[7,4,1],[8,5,2],[9,6,3]]

        copy = [row[:] for row in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix)-1, -1, -1):
                matrix[i][len(matrix) -j -1] = copy[j][i]
                # print(matrix)
        print(matrix)

trial = Solution()
trial.rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

        