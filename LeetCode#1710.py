class Solution:
    def maximumUnits(self, boxTypes, truckSize) -> int:
        boxTypes.sort(
            key=lambda box_type: box_type[1], reverse=True)

        loaded_fully = False
        count = 0
        i = 0
        while not loaded_fully:
            if boxTypes[i][0] > 0:
                count += boxTypes[i][1]
                boxTypes[i][0] -= 1
                truckSize -= 1
            else:
                i += 1

            if truckSize == 0:
                loaded_fully = True

        return count


trial = Solution()
o = trial.maximumUnits(
    boxTypes=[[5, 10], [2, 5], [3, 9], [4, 7]], truckSize=10)
print(o)
