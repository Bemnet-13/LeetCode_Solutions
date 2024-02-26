class Solution:
    def validIPaddress(self, address_split):
        self.address_split = address_split
        for x in address_split:
            if not 0 <= int(x) <= 255:
                return False
        return True

    def defangIPaddr(self, address):
        self.address = address
        address_split = self.address.split(".")
        if self.validIPaddress(address_split):
             return "[.]".join(address_split)
        

trial = Solution()
print(trial.defangIPaddr("255.100.50.0"))