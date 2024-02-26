class Solution:
    def findWinners(self, matches):
        # Use list comprehension to find losers and winners
        # Use set to filter the players
        # if a player is in winners but not in losers, append it to winners
        # if a player count in losers is exactly 1, append it to the other list

        winners = [i[0] for i in matches]
        losers = [i[1] for i in matches]

        win = list(set(winners)-set(losers))
        los_1 = []
        for j in set(losers):
            if losers.count(j) == 1:
                los_1.append(j)
        
        answer = []
        answer.append(win)
        answer.append(los_1)
        return answer

trial = Solution()
o = trial.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]])
print(o)