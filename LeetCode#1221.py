class Solution:
    def is_balanced(self, string):
        self.string = string
        total = self.string.count('R') + self.string.count('L')
        if len(self.string) % 2 == 0 and 2 <= len(self.string) <= 1000:
            if self.string.count('R') == self.string.count('L') and total == len(self.string):
                return True
            return False
        return False

    def balancedStringSplit(self, s):
        self.s = s
        string = self.s
        n = 2
        count = 0
        while n <= len(string):
            chunks = [self.s[i: i+n] for i in range(0, len(self.s), n)]
            for substring in chunks:
                other_chunks = chunks[:]
                other_chunks.remove(substring)
                rejoined_chunks = "".join(other_chunks)
                if self.is_balanced(substring) and self.is_balanced(rejoined_chunks):
                    count += 1
                    chunks.remove(substring)
            if len(self.s) == 0:
                remaining = False
            self.s = string
            n += 2

        return count


user_input = input("Input: ")
user_string = Solution()
output = user_string.balancedStringSplit(user_input)
print(f"Output: {output}")
