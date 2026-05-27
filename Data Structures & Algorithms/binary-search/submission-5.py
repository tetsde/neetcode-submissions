class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1 
        while hi >= lo:
            mid_index = (lo + hi)//2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                   hi = mid_index - 1  
            else:
                   lo = mid_index + 1 
        return -1 