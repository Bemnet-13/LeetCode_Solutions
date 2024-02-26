class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0
        for string in words:
            string_set = set(string)
            if string_set.issubset(allowed_set):
                count += 1

        return count


trial = Solution()
output = trial.countConsistentStrings(
    allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"])
print(output)
