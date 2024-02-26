class Solution:
    def minDeletions(self, s: str) -> int:
        app = {}
        for letter in s:
            if letter in app:
                app[letter] += 1
            else:
                app[letter] = 1

        [3,3,2]

        freq = list(app.values())
        freq.sort(reverse=True)
        unique_freq = set(freq)
        op1 = sum(freq) - sum(unique_freq)
        checked = []
        count = 0
        i = 0

        while i < len(freq):
            if freq[i] in freq[i:] or (freq[i] in checked and freq[i] != 0):
                freq[i] -= 1
                count += 1
            else:
                checked.append(freq[i])
                i += 1
        
        unique_freq = set(freq)

        return min(count,op1)
    
