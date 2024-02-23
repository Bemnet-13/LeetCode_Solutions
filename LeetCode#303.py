class NumArray:

    def __init__(self, nums):
        self.p_sum = [0]
        for num in nums:
            self.p_sum.append(self.p_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.p_sum[right + 1]
        leftSum = self.p_sum[left]

        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)