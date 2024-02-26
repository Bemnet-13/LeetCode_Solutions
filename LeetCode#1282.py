class Solution:
    def groupThePeople(self, groupSizes):
        # Sort the list in descending order
        # Iterate through the list and append the enumerate objects to the list
        # Iterate through the list AND APPEND each who belong in the same group
        # if the length is going to overfolw, append it to a list form a new array each time


        
        new_arr = list(enumerate(groupSizes))
        new_arr.sort(key= lambda item :item[1], reverse=True)
        groupList = []
        arr = []
        for i in range(len(new_arr)):
            item = new_arr[i]
            member = item[0]
            size = item[1]
            if len(arr) < size:
                arr.append(member)
            else:
                groupList.append(arr)
                arr = []
                arr.append(member)
            if i == len(new_arr) - 1:
                groupList.append(arr)
        print(groupList)
        
        

trial = Solution()
o = trial.groupThePeople([2,1,3,3,3,2])
print(o)