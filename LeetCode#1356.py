class Solution:
    def sortByBits(self, arr):
        num_1_bits = []
        arr.sort()
        for num in arr:
            num_1_bits.append(self.totalBits(num))

        combined = list(zip(arr, num_1_bits))

        combined.sort(key=lambda num: num[1])

        for i in range(len(arr)):
            arr[i] = combined[i][0]

        return arr

    def totalBits(self, n):
        bits = self.DecimalToBinary(n)
        return bits.count("1")

    def DecimalToBinary(self, n):
        if n // 2 == 0:
            return str(n % 2)
        return self.DecimalToBinary(n // 2) + str(n % 2)


trial = Solution()
print(trial.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]))
