class Solution:
    def findJudge(self, n: int, trust) -> int:
        # Intuition
        # Find the trusters as a set
        # Find the trustees as a set
        # Use set difference trustees - trusters
        # If the set is empty, return -1
        # If not return the first element in the set
        trusters = set()
        trustees = set()
        trusted = []
        for p1, p2 in trust:
            trusters.add(p1)
            trustees.add(p2)
            trusted.append(p2)

        possible_judge = trustees - trusters

        if possible_judge == {}:
            return -1
        
        for judge in possible_judge:
            if trusted.count(judge) == n - 1:
                return judge
            else:
                return -1