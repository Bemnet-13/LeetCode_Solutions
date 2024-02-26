class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        l = 0
        r = 0
        content_no = 0
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                content_no += 1
                l += 1
                r += 1
            else:
                r += 1
        
        return content_no