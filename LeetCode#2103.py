class Solution:
    def countPoints(self, rings):
        appearance_lst = [''] * 10
        for i in range(1, len(rings), 2):
            j = int(rings[i])
            appearance_lst[j] += rings[j-1] 
        
        count = 0
        for ring in appearance_lst:
            if 'R' in ring and 'G' in ring and 'B' in ring:
                count += 1
        
        return count
        
        

        
        
