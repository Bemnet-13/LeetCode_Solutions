class Solution:
    def generate(self, numRows: int):
        # Initialize a Pascal triangle with numRows = 2 and 1
        # run a while loop until len(pascalTri) == numRows
        # Create a list with length p + 1 and append it to pascalTri
        # return pascalTri

        pascalTri = [[1], [1,1]]
        if numRows <= 2:
            return pascalTri[:numRows+1]
        
        i = 1
        while len(pascalTri) < numRows:
            newRow = ["*"] * i + 2
            newRow[0] , newRow[-1] = pascalTri[i][0], pascalTri[i][-1]
            for j in range(1,len(newRow)):
                newRow[j] = pascalTri[i][j] + pascalTri[i][j-1]
            pascalTri.append(newRow)
        return pascalTri
    



