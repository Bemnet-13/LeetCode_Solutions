class Solution:
    def restoreString(self, s, indices):
        self.s = s
        self.indices = indices
        if self.is_string_valid(self.s, self.indices):
            new_list = ["*"] * len(self.s)
            for i in range(len(self.indices)):
                ind = self.indices[i]
                new_list[ind] = self.s[i]

            shuffled_string = "".join(new_list)
            return shuffled_string

    def is_string_valid(self, s, list):
        self.s = s
        self.list = list
        n = len(self.s)
        valid = False
        if len(self.list) == n and 1 <= n <= 100:
            valid = True

        if valid:
            for ind in range(n):
                if ind not in list:
                    return not valid
            return valid
        return False


trial1 = Solution()
user_string = input("Input: s = ").lower()
user_indices = eval(input("indices = "))
output = trial1.restoreString(user_string, user_indices)
print(f"Output: {output}")
