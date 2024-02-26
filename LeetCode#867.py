class Solution:
    def transpose(self, matrix):
        # Intuition
        # Use indices array and iterate through the list and append the result to each transpose

        indices = [i for i in range(len(matrix[0]))]

        transpose = []
        for i in range(len(matrix[0])):
            col = []
            for arr in matrix:
                col.append(arr[i])
            transpose.append(col)
        return transpose
