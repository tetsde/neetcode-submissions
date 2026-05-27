class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tienTo = 1
        hauTo = 1
        result = [1] * n

        for i in range(n):
            result[i] = tienTo
            tienTo *= nums[i]

        for i in range(n-1, -1, -1):
            result[i] *= hauTo
            hauTo *= nums[i]

        return result