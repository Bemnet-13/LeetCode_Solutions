class Solution:      
    def minOperations(self, s):
        output1 = self.alternatingCounter(s,True)
        output2 = self.alternatingCounter(s,False)
        return min(output1, output2)

    def alternatingCounter(self, s, flag):
        arr = []
        counter = 0
        for i in range(len(s)):
            if len(arr) == 0 and flag == True:
                if s[i] == "0":
                    arr.append("1")
                else:
                    arr.append("0")
                counter += 1
            elif len(arr) == 0:
                arr.append(s[i])
            # For the remaining items
            if arr[-1] != s[i]:
                arr.append(s[i])
            else:
                if arr[-1] == "0":
                    arr.append("1")
                    counter += 1
                else:
                    arr.append("0")
                    counter += 1
        
        return counter
    

    
trial = Solution()
o = trial.minOperations("1111")
print(o)

  # # 1
        # Itearte throught the list
        # Push the element to the stack
        # If the element at the top and the next element are
        # not identical-- pop the item off the list
        # If identical, increment a counter and pop the element off the list

        # if len(s) == 1:
        #     return 0
        
        # stack = []
        # counter = 0
        # stack.append(s[0])
        # for i in range(1, len(s)):
        #     if stack[-1] != s[i]:
        #         stack.pop()
        #         stack.append(s[i])
        #     else:
        #         stack.pop()
        #         counter += 1
        #         stack.append(s[i])
        
        # return counter

        # 2
        # Set an empty list
        # Append the first item to the list
        # Iterate through the string and 
        #  if the last item on arr is d/t from ---
        # -----append it
        # else
        # invert the last item and append it to the list and increment the counter by one

