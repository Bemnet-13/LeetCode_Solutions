class Solution:
    def numberOfBeams(self, bank) -> int:
        # Set two pointers l and r and an accumulator acc
        # Iterate through arr and r = l + 1
        # if arr[r].count('1')*arr[r].count('1') != 0 acc+=
        # else r += 1

        l = 0
        r = l + 1
        acc = 0
        while l < len(bank) and r < len(bank):
            lasers = bank[l].count('1') * bank[r].count('1')
            if lasers != 0:
                acc += lasers
                l = r
                r = l + 1
            else:
                r += 1
        
        return acc
    
trial = Solution()
o = trial.numberOfBeams(bank = ["000","111","000"])
print(o)