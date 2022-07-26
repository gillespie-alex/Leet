class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # do a forward pass and a backward pass
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        f_sum, b_sum = 1, 1
        for i in range(len(nums)):
            forward[i] = f_sum
            f_sum *= nums[i]
        for i in reversed(range(len(nums))):
            backward[i] = b_sum
            b_sum *= nums[i]
        return [forward[i] * backward[i] for i in range(len(nums))]
        