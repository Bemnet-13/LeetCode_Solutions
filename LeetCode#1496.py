class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Intuition
        # Choose the origin to be [0,0] 
        # Increment the appropriate integer in the index for each direction
        # Each time we move check if the direction is already in the movement matrix
        # return False if that's the case

        x = 0
        y = 0      
        coordinates = [(0,0)]

        for i in path:
            if i == "N":
                y += 1
            elif i == "E":
                x += 1
            elif i == "W":
                x -= 1
            else:
                y -= 1
            
            coordinate = x, y
            if coordinate in coordinates:
                return True
            else:                
                coordinates.append(coordinate)
        
        return False

trial = Solution()
o = trial.isPathCrossing("NESWW")
print(o)