class Solution:
    def destCity(self, paths) -> str:
        # Intuition
        # Construct two set sets from the initial points
        # Return the peculiar element


        initial = set([city[0] for city in paths])
        final = set([city[1] for city in paths])

        destination_ct =  final.difference(initial)
        for i in destination_ct:
            return i
trial = Solution()
o = trial.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(o)