class Solution:
    def garbageCollection(self, garbage, travel) -> int:
        # Write a function that takes three parameters garbage, sum, garbageType
        # It sums up the time required by iterating through the list and counting the amount of spe. garbage 
        # return it to the main function
        time = [0]
        for i in range(len(travel)):
            time.append(time[-1] + travel[i])
        return self.garbageTypeCollector(garbage, time, type="M")+ self.garbageTypeCollector(garbage, time, type="G")+ self.garbageTypeCollector(garbage, time, type="P")

    
    def garbageTypeCollector(self, garbage, time, type):
        garbageCount = 0
        stopper = 0
        for i in range(len(garbage)):
            if type in garbage[i]:
                stopper = i
                garbageCount += garbage[i].count(type)
        
        return garbageCount + time[stopper]

trial = Solution()
o = trial.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])
print(o)