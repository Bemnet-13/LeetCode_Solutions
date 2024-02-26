class Solution:
    def deleteGreatestValue(self, grid) -> int:
        for row in grid:
            row.sort()

        NO_COLUMNS = len(grid[0])
        max_del = 0
        for j in range(NO_COLUMNS - 1, -1, -1):
            del_list = []
            for i in range(len(grid)):
                del_element = grid[i].pop()
                del_list.append(del_element)
            max_del += max(del_list)

        return max_del
    
trial = Solution()
print(trial.deleteGreatestValue(grid = [[1,2,4],[3,3,1]]))
