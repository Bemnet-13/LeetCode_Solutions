class Solution:
    def minimumSum(self, num: int) -> int:
        num_arr = []
        while num > 0:
            rem = num % 10
            num = num // 10
            num_arr.append(rem)

        num_arr.sort()
        i = 0
        first = 10 * num_arr[i] + num_arr[i + 2]
        second = 10 * num_arr[i + 1] + num_arr[i + 3]
        return first + second
