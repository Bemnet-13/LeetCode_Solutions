class Solution:
    def totalFruit(self, fruits) -> int:
        # Define empty list
        # Iterate through fruits
        # Use the number of unique fruits variable when iterating through
        # If the element is in the list append it 
        # If not pop the first item and continue
        

        fruit_trees = []
        unique_fruits = 1
        i = 0
        max_fruits = 1
        while i < len(fruits):
            fruit = fruits[i]
            if unique_fruits < 2:
                fruit_trees.append(fruit)
                unique_fruits = len(set(fruit_trees))
                i += 1
            elif fruit in fruit_trees:
                fruit_trees.append(fruit)
                i += 1
            else:
                fruit_trees.pop(0)
            unique_fruits = len(set(fruit_trees))

            max_fruits = max(max_fruits, len(fruit_trees))
        return max_fruits
trial = Solution()
o = trial.totalFruit(fruits = [1,2,3,2,2])            
print(o)