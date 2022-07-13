class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_array = [0]*len(self.nums)
        self.prefix_array[0] = self.nums[0]
        for i in range(1,len(self.nums)):
            self.prefix_array[i] = self.nums[i] + self.prefix_array[i-1]
        print(self.prefix_array)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_array[right] if left == 0 else \
                    self.prefix_array[right] - self.prefix_array[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)