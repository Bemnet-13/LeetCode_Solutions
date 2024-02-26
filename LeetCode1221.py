class Solution:
    def is_balanced(self, string):
        self.string = string
        total = self.string.count('R') + self.string.count('L')
        if len(self.string) % 2 == 0:
            if self.string.count('R') == self.string.count('L') and total == len(self.string):
                return True
            return False
        return False

    
    def balancedStringSplit(self, s: str) -> int:
        chunks = [s[i : i+2] for i in range(0, len(s), 2)]
        balanced = []
        for i in range(len(chunks)):
            if self.is_balanced(chunks[i]):
                chunk = chunks.pop(i)
                if self.is_balanced("".join(chunks)):
                    balanced.append(chunk)
                else:
                    chunks.insert(i, chunk)
            else:
                chunks[i] = chunks[i] + chunks[i+1]

        return len(balanced)