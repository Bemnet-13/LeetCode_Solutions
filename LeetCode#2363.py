class Solution:
    def mergeSimilarItems(self, items1, items2):
        _items1_0 = [item[0] for item in items1]

        for item in items2:
            if item[0] not in _items1_0:
                items1.append(item)
            else:
                i = item[1]
                for j in items1:
                    if j[0] == item[0]:
                        j[1] = j[1] + i
        
        return items1

trial = Solution()
output = trial.mergeSimilarItems(
    items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]])
print(output)