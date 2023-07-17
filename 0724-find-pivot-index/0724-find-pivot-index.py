class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        pivot_index = 0
        while pivot_index < len(nums) and left_sum != total_sum -left_sum - nums[pivot_index]:
            left_sum += nums[pivot_index]
            pivot_index += 1
        if pivot_index == len(nums):
            return -1
        else: 
            return pivot_index
        
        