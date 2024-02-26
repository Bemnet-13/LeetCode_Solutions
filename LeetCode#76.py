class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Intuition
        # Use enumerate to find the occurences of each letters in t
        # Split the string t into list 
        # store it inside other variable
        # iterate through the the indexed list and find each occurences
        # store the first var in i and pop each chr from t 
        # if t is empty append the len subarray of the from i to the currrent index 
        # find the max of the list


        indexed_chr = list(enumerate(s))
        t_lst = list(t)

        for app in indexed_chr:
            idx = app[0]
            chr = app[1]

            if chr not in t:
                indexed_chr.remove(app)
        
        valid_len = []
        store = t_lst
        i = 0

        while i < len(indexed_chr):
            if len(t_lst) == len(store):
                k = indexed_chr[i][0]
            
            t_lst.remove(indexed_chr[i][1])

            if t_lst == []:
                substring = s[k:indexed_chr[i][0] + 1]
                valid_len.append(len(substring))
                t_lst = store
            i += 1

            return min(valid_len)
