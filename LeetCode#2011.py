class Solution:
    def finalValueAfterOperations(self, operations):
        operand_values = {"X++": 1, "++X": 1, "--X": -1, "X--": -1}
        x = 0
        for operation in operations:
            x += operand_values[operation]

        return x
